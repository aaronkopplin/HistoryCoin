clear
#solc HistoryCoin.sol --abi > HistoryCoinAbi
#solc HistoryCoin.sol --bin > HistoryCoinBin

solc HistoryCoin.sol --combined-json abi,bin | python -m json.tool > HistoryCoinAbiBin.json