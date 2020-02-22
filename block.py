from web3 import Web3
import json
import pandas as pd
csvData = pd.read_csv("data.csv")
csvData = csvData.dropna()
mac_list = csvData.Mac.tolist()
data_list = csvData.Data.tolist()
web3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
print("Connected to blockchain: ",web3.isConnected())
print("----------------------------------------------")
with open('build/contracts/StoreData.json') as f:
  data = json.load(f)
  bytecode = data['bytecode']
  data = data['abi']
# abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"},{"name":"","type":"uint256"}],"name":"mainData","outputs":[{"name":"ldata","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_mac","type":"uint256"}],"name":"addEvent","type":"event"},{"constant":false,"inputs":[{"name":"_mac","type":"uint256"},{"name":"_ldata","type":"uint256"}],"name":"addData","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
abi = data
web3.eth.defaultAccount = web3.eth.accounts[0]
StoreData = web3.eth.contract(bytecode=bytecode, abi=abi)
tx_hash = StoreData.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
contract = web3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
contract.functions.addData("00:0a:95:9d:68:16",111).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
count = contract.functions.getCount("00:0a:95:9d:68:16").call()
print("MAC","\t\t","Data")
for i in range(0,count):
    print("00:0a:95:9d:68:16",contract.functions.getData("00:0a:95:9d:68:16",i).call())
count = contract.functions.getCount("00:0b:25:3d:62:16").call()
for i in range(0,count):
    print("00:0b:25:3d:62:16",contract.functions.getData("00:0b:25:3d:62:16",i).call())

macList = {}
# 0 - active
# 1 - greylisted(wildcard)
# 2 - blacklisted