from SmartContract.BaseHistoryCoinContract import BaseHistoryCoinContract


class HistoryCoinContract(BaseHistoryCoinContract):
    def __init__(self):
        super().__init__()

    def APY(self):
        return self.contract.functions.APY().call()

    def CreateRecord(self, text, votingLifetimeInBlocks):
        tx_hash = self.contract.functions.CreateRecord(text, votingLifetimeInBlocks).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def allowance(self, _owner, _spender):
        return self.contract.functions.allowance(_owner, _spender).call()

    def allowed(self):
        return self.contract.functions.allowed().call()

    def approve(self, _spender, _value):
        tx_hash = self.contract.functions.approve(_spender, _value).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def averageTotalVotesPerRecord(self):
        return self.contract.functions.averageTotalVotesPerRecord().call()

    def balanceOf(self, _owner):
        return self.contract.functions.balanceOf(_owner).call()

    def balances(self):
        return self.contract.functions.balances().call()

    def decimals(self):
        return self.contract.functions.decimals().call()

    def farmVote(self, record_id, voter_address):
        tx_hash = self.contract.functions.farmVote(record_id, voter_address).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def getBalance(self):
        return self.contract.functions.getBalance().call()

    def getRecordVoterArray(self, id):
        return self.contract.functions.getRecordVoterArray(id).call()

    def mintTokens(self):
        tx_hash = self.contract.functions.mintTokens().transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def name(self):
        return self.contract.functions.name().call()

    def numRecords(self):
        return self.contract.functions.numRecords().call()

    def records(self):
        return self.contract.functions.records().call()

    def symbol(self):
        return self.contract.functions.symbol().call()

    def totalSupply(self):
        return self.contract.functions.totalSupply().call()

    def transfer(self, _to, _value):
        tx_hash = self.contract.functions.transfer(_to, _value).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def transferFrom(self, _from, _to, _value):
        tx_hash = self.contract.functions.transferFrom(_from, _to, _value).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def vote(self, id, vote_value, security_deposit):
        tx_hash = self.contract.functions.vote(id, vote_value, security_deposit).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

