from web3 import Web3

# Connecting Ethereum Nodes
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Wallet Information
account = w3.eth.account.from_key("YOUR_PRIVATE_KEY")

# Importing compiled smart contract ABI and bytecode
with open("CasinoBet_abi.json") as f:
    contract_abi = f.read()
with open("CasinoBet_bytecode.txt") as f:
    contract_bytecode = f.read()

# Contract deployment
CasinoBet = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = CasinoBet.constructor("0x" + merkle_root).transact({'from': account.address, 'gas': 5000000})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
print(f"Contract Deployed at: {contract_address}")

# Merkle root update
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
tx_hash = contract.functions.updateMerkleRoot("0x" + merkle_root).transact({'from': account.address})
w3.eth.wait_for_transaction_receipt(tx_hash)
print("Merkle Root Updated!")
