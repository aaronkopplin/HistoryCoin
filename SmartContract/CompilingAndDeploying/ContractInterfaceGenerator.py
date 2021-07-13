import json

contract_json = open("HistoryCoinAbiBin.json", "r")
data = json.load(contract_json)
abi = data["contracts"]["../HistoryCoin.sol:HistoryCoin"]["abi"]

generated_class = open("../HistoryCoinContract.py", "w")
generated_class.write("from SmartContract.BaseHistoryCoinContract import BaseHistoryCoinContract"
                      "\n\nclass HistoryCoinContract(BaseHistoryCoinContract):\n"
                      "    def __init__(self):\n"
                      "        super().__init__()\n\n")

for attribute in abi:
    if attribute["type"] == "function":
        line = ""
        if attribute.get("name"):
            line += "    def " + attribute["name"] + "(self"
            parameters = ""
            if len(attribute["inputs"]) > 0:
                for input in attribute["inputs"]:
                    if input["name"] != "":
                        parameters += ", " + input["name"]
                # line = line[:-2]
            line += parameters
            line += "):\n       "

            if attribute.get("stateMutability"):
                if attribute["stateMutability"] == "view":
                    line += "return self.contract.functions." + attribute["name"] + "(" + parameters[2:] + ").call()\n\n"
                else:
                    line += "tx_hash = self.contract.functions." + attribute["name"] + "(" + parameters[2:] + \
                            ").transact()\n       self.w3.eth.wait_for_transaction_receipt(tx_hash)\n\n"

            generated_class.write(line)
