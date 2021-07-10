// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.4;

library VoteList {
    Vote head;

    struct vote {
        address owner;
        uint value;
    }

    struct List {
        uint size;

    }
}