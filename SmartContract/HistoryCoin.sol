// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.4;
pragma experimental ABIEncoderV2;

//import "./ERC20Contract.sol";
import "./Libraries/SafeMath.sol";
//import "./VoteList.sol";

contract HistoryCoin {

    using SafeMath for uint;

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

    uint256 constant             private MAX_UINT256 = 2**256 - 1;
    mapping (address => uint256) public balances;
    mapping (address => mapping (address => uint256)) public allowed;
    string                       public name;  //fancy name: eg Simon Bucks
    uint8                        public decimals;  //How many decimals to show.
    string                       public symbol;  //An identifier: eg SBX
    uint                         public totalSupply;

    uint                         private BLOCKS_PER_YEAR = 2407328;
    uint                         public  APY = 5;
    uint                         public  numRecords = 0;
    mapping(uint => Record)      public  records;
    uint                         private numActiveRecords = 0;
    uint                         private numInactiveRecords = 0;
    uint                         public  averageTotalVotesPerRecord = 0;

    struct Vote {
        uint vote_amount;
        uint security_deposit; // allows anyone to claim the deposit for returning your stake
    }

    struct Record {
        string text;
        uint votingLifetimeInBlocks;
        uint blockProposed;
        mapping(address => Vote) votes;
        address[] voters;
        uint id;
        bool expired;
        uint totalVotes;
        uint interest_rate;
        address owner;
        uint security_deposit;
    }

    constructor(){
        // balances[msg.sender] = 100000000;               // Give the creator all initial tokens
        totalSupply = 1000000;                        // Update total supply
        name = "History Coin";                                   // Set the name for display purposes
        decimals = 18;                            // Amount of decimals for display purposes
        symbol = "HIST";                               // Set the symbol for display purposes
    }

    function transfer(address _to, uint256 _value) public  returns (bool success) {
        require(balances[msg.sender] >= _value);
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public  returns (bool success) {
        uint256 amountAllowed = allowed[_from][msg.sender];
        require(balances[_from] >= _value && amountAllowed >= _value);
        balances[_to] += _value;
        balances[_from] -= _value;
        if (amountAllowed < MAX_UINT256) {
            allowed[_from][msg.sender] -= _value;
        }
        emit Transfer(_from, _to, _value);
        return true;
    }

    function balanceOf(address _owner) public  view returns (uint256 balance) {
        return balances[_owner];
    }

    function approve(address _spender, uint256 _value) public  returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public  view returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }

    /* Users can create records, which are publicly available for
       voting. When record voting lifetimes expire, the original stake
       will be returned to the voter, plus interest.  */
    function createRecord(string memory text, uint16 votingLifetimeInBlocks) public payable{
        if (votingLifetimeInBlocks > BLOCKS_PER_YEAR) {
            // roughly one year at 13.1 seconds for block time
            revert("lifetimes greater than one year (2407328 blocks) are not allowed.");
        }

        records[numRecords].text = text;
        records[numRecords].votingLifetimeInBlocks = votingLifetimeInBlocks;
        records[numRecords].blockProposed = block.number;
        records[numRecords].voters.push(msg.sender);
        records[numRecords].votes[msg.sender] = Vote(0, 0);
        records[numRecords].id = numRecords;
        records[numRecords].expired = false;
        records[numRecords].owner = msg.sender;
        records[numRecords].security_deposit = msg.value;

        numRecords++;
        numActiveRecords++;
    }

    /* The act of voting automatically stakes your vote until the end
       of the lifetime of the record. Once the voting period has
       ended, the original stake, plus interest (in HIST) will be
       returned to the staker */
    function vote(uint record_id, uint vote_value, uint security_deposit) external payable {
        require(!records[record_id].expired);
        require(balances[msg.sender] >= vote_value);
        require(msg.value == security_deposit);

        balances[msg.sender] -= vote_value;
        records[record_id].votes[msg.sender].vote_amount += vote_value;
        records[record_id].votes[msg.sender].security_deposit += security_deposit;
        records[record_id].totalVotes += vote_value;
    }

    /* a record must expire before its votes can be farmed  */
    function farmRecord(uint record_id) public {
        require(!records[record_id].expired);
        require (records[record_id].blockProposed + records[record_id].votingLifetimeInBlocks < block.number);

        records[record_id].expired = true;
        averageTotalVotesPerRecord = (averageTotalVotesPerRecord + records[record_id].totalVotes) / numRecords;
        records[record_id].interest_rate = 10; // TODO

        balances[msg.sender] += records[record_id].security_deposit;
        records[record_id].security_deposit = 0;
    }

    /* vote farming is the process if returning the vote stake to the original staker. This
     process costs gas, so it cannot be done randomly. the vote security deposit is an incentive
     for someone to farm the vote. the security deposit should be higher than the gas cost to farm the
     vote, or else it will take a long time to return the stake. the higher the security deposit, the greater
     incentive there is to return the stake, and thus the faster the stake will be returned once the
     record has expired. */
    function farmVote(uint record_id, address voter_address) public {
        require (records[record_id].expired);

        // return the stake to the staker
        uint interest = records[record_id].interest_rate;
        issueNewTokens(records[record_id].votes[voter_address].vote_amount + interest, voter_address);

        // pay the security deposit to the vote farmer
        (bool success, ) = msg.sender.call{value:(records[record_id].votes[voter_address].security_deposit)}("");
        require(success, "Transfer failed.");

        // clear the balances of the vote
        records[record_id].votes[voter_address].vote_amount = 0;
        records[record_id].votes[voter_address].security_deposit = 0;
    }

    /* function getRecordVoteArray(uint id) public view returns(uint[] memory) {
        uint length = records[id].voters.length;
        uint[] memory votes = new uint[](length);

        for(uint i = 0; i < length; i++) {
            address voter = records[id].voters[i];
            votes[i] = records[id].votes[voter];
        }

        return votes;
    } */

    function getRecordVoterArray(uint id) public view returns(address[] memory) {
        return records[id].voters;
    }

    function issueNewTokens(uint amount, address recipient) private {
        balances[recipient] += amount;
        totalSupply += amount;
    }

    function buyTokens() public payable {
        require(msg.value >= 0);
        issueNewTokens(msg.value, msg.sender);
    }
//
//    function sellTokens(uint amount) public {
//        require(amount <= balances[msg.sender]);
//        balances[msg.sender] -= amount;
//        // return eth to seller
//
//    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}