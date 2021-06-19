clear
#solc HistoryCoin.sol --abi > HistoryCoinAbi
#solc HistoryCoin.sol --bin > HistoryCoinBin

solc HistoryCoin.sol --combined-json abi,bin | python3 -m json.tool > HistoryCoinAbiBin.json