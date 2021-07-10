clear

solc ../HistoryCoin.sol
solc ../HistoryCoin.sol --combined-json abi,bin | python3 -m json.tool > HistoryCoinAbiBin.json


