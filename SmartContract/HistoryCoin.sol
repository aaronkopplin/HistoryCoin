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

    uint256 constant private MAX_UINT256 = 2**256 - 1;
    mapping (address => uint256) public balances;
    mapping (address => mapping (address => uint256)) public allowed;
    string public name;  //fancy name: eg Simon Bucks
    uint8 public decimals;  //How many decimals to show.
    string public symbol;  //An identifier: eg SBX
    uint public totalSupply;

    uint BLOCKS_PER_YEAR = 2407328;
    uint APY = 5;
    uint numRecords = 0;
    mapping(uint => Record) public records;
    uint private numActiveRecords = 0;
    uint private numInactiveRecords = 0;
    string public message = "Hello world";

    struct Record {
        string text;
        uint votingLifetimeInBlocks;
        uint blockProposed;
        mapping(address => uint) votes;
        address[] voters;
        uint id;
        bool expired;
    }

    constructor(){
//        balances[msg.sender] = 100000000;               // Give the creator all initial tokens
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
    function CreateRecord(string memory text, uint16 votingLifetimeInBlocks) public {
        if (votingLifetimeInBlocks > BLOCKS_PER_YEAR) {
            // roughly one year at 13.1 seconds for block time
            revert("lifetimes greater than one year (2407328 blocks) are not allowed.");
        }

        records[numRecords].text = text;
        records[numRecords].votingLifetimeInBlocks = votingLifetimeInBlocks;
        records[numRecords].blockProposed = block.number;
        records[numRecords].voters.push(msg.sender);
        records[numRecords].votes[msg.sender] = 0;
        records[numRecords].id = numRecords;
        records[numRecords].expired = false;

        numRecords++;
        numActiveRecords++;
    }

    /* The act of voting automatically stakes your vote until the end
       of the lifetime of the record. Once the voting period has
       ended, the original stake, plus interest (in HIST) will be
       returned to the staker  */
    function Vote(uint id, uint value) external payable {
        require(records[id].expired);
        require(balances[msg.sender] >= value);

        balances[msg.sender] -= value;
        records[id].votes[msg.sender] += value;

        for (uint i = 0; i < numRecords; i++) {
            // iterate over all the records that have not expired yet
            if (records[id].blockProposed + records[id].votingLifetimeInBlocks < block.number && !records[id].expired) {
                records[i].expired = true;

                // release the staked funds plus interest
                Record storage currentRecord = records[i];
                for (uint j = 0; j < currentRecord.voters.length; j++) {
                    address voterAddress = currentRecord.voters[j];
                    returnStake(voterAddress, i);
                }
            }
        }
    }

    function returnStake(address voterAddress, uint id) private {
        // return the stake
        uint tokens = records[id].votes[voterAddress];
        balances[voterAddress] += tokens;

        uint interest = tokens * (APY * records[id].votingLifetimeInBlocks.div(BLOCKS_PER_YEAR)).div(100);
        // issue some interest payment
        balances[voterAddress] += interest;
        totalSupply += interest;

        //emit stakeReturned();
    }

    function requestTokens(uint amount) public {
        balances[msg.sender] += amount;
        totalSupply += amount;
    }


    /* function GetRecord(uint id) public view returns (Record storage) {
        return records[id];
    } */

    function GetNumberOfRecords() public view returns (uint) {
        return numRecords;
    }

    function GetMessage() public view returns (string memory) {
        return message;
    }

    function SetMessage(string memory newMessage) public {
        message = newMessage;
    }
}