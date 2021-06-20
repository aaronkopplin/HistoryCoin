// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.4;
pragma experimental ABIEncoderV2;

contract HistoryCoin {

    struct record {
        string text;
        uint16 lifetimeInBlocks;
        uint blockProposed;
        uint votes;
        uint id;
    }

    event RecordProposalReceived();
    record[] records;
    uint count;
    string message = "Hello world";

    constructor() {}

    function Vote(uint id) external payable {
        if (block.number < records[id].blockProposed + records[id].lifetimeInBlocks) {
            records[id].votes += msg.value;
        } else {
            revert("record is no longer available for voting.");
        }
    }

    function MakeProposal(string memory text, uint16 lifetimeInBlocks) public returns (uint){
        if (lifetimeInBlocks > 2407328 ) {
            // roughly one year at 13.1 seconds for block time
            revert("lifetimes greater than one year (2407328 blocks) are not allowed.");
        }
        records.push(record(text, lifetimeInBlocks, block.number, 0, count++));
        emit RecordProposalReceived();
        return records[count - 1].id;
    }

    function GetRecord(uint id) public view returns (record memory) {
        return records[id];
    }

    function GetNumberOfRecords() public view returns (uint) {
        return count;
    }

    function GetMessage() public view returns (string memory) {
        return message;
    }

    function SetMessage(string memory newMessage) public {
        message = newMessage;
    }

//    function IssueTokens() {}
    
}