// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.4;
pragma experimental ABIEncoderV2;

import "./ERC20Contract.sol";
import "./SafeMath.sol";

abstract contract HistoryCoin is ERC20Contract(
    100000000, 
    "History Coin", 
    18, 
    "Hist") {

    using SafeMath for uint;

    uint BLOCKS_PER_YEAR = 2407328;
    uint APY = 5;
    record[] public records;
    uint private numActiveRecords = 0;
    uint private numInactiveRecords = 0;
    string public message = "Hello world";
    
    struct record {
        string text;
        uint votingLifetimeInBlocks;
        uint blockProposed;
        vote[] votes;
        uint id;
        bool expired;
    }

    struct vote {
        address owner;
        uint value;
    }

    // event RecordReceived(
    //     string text,
    //     uint16 votingLifetimeInBlocks
    // );

    /* *************************************************************** */
    /* Users can create records, which are publicly available for
       voting. When record voting lifetimes expire, the original stake
       will be returned to the voter, plus interest.                   */
    /* *************************************************************** */
    function CreateRecord(string memory text, uint16 votingLifetimeInBlocks) public {
        if (votingLifetimeInBlocks > BLOCKS_PER_YEAR) {
            // roughly one year at 13.1 seconds for block time
            revert("lifetimes greater than one year (2407328 blocks) are not allowed.");
        }

        vote[] memory votes;
        records.push(record(text, votingLifetimeInBlocks, block.number, votes, records.length + 1, false));
        numActiveRecords++;
    }
    
    /* *************************************************************** */
    /*  The act of voting automatically stakes your vote until the end */
    /*  of the lifetime of the record. Once the voting period has      */
    /*  ended, the original stake, plus interest (in HIST) will be     */
    /*  returned to the staker.                                        */
    /* *************************************************************** */
    function Vote(uint id) external payable {
        if (isRecordExipired(id)) {
            revert("record is no longer available for voting.");
        }
        
        balances[msg.sender] -= msg.value;
        records[id].votes.push(vote(msg.sender, msg.value));

        if (numActiveRecords > numInactiveRecords) {
            // check to see if any need to be expired
            for (uint i = 0; i < records.length; i++) {
                if (isRecordExipired(i)) {
                    records[i].expired = true;
                    // release the staked funds plus interest
                    for (uint j = 0; j < records[i].votes.length; j++) {
                        vote memory currentVote = records[i].votes[j];
                        balances[currentVote.owner] += currentVote.value;
                        // issue some interest payment
                        balances[currentVote.owner] +=  APY * (records[i].votingLifetimeInBlocks.div(BLOCKS_PER_YEAR));
                    }
                }
            }
        }
    }

    function isRecordExipired(uint id) public view returns (bool expired){
        if (records[id].expired || block.number >= records[id].blockProposed + records[id].votingLifetimeInBlocks) {
            return true;
        }

        return false;
    }

    function GetRecord(uint id) public view returns (record memory) {
        return records[id];
    }

    function GetNumberOfRecords() public view returns (uint) {
        return records.length;
    }

    function GetMessage() public view returns (string memory) {
        return message;
    }

    function SetMessage(string memory newMessage) public {
        message = newMessage;
    }
    
}