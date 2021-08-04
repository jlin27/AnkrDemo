import os
import json
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER']
w3 = Web3(Web3.HTTPProvider(node_provider))

# Confirms if the connection succeeded 
def is_connected():
    return w3.isConnected()

# Use the contract abi and address to connect to an instace of the contract.
# The contract abi is the json representatin of our smart contract
# and it it used for our code to know how to interact with our smart contract.
# The contract address is used to locate our smart contract.
contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_address = w3.toChecksumAddress(os.environ['CONTRACT_ADDRESS'])
contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# The nonce is the number of transactions from a given address
# Used against double-spending
def get_nonce(ETH_address):
    return w3.eth.get_transaction_count(ETH_address)

# Calls getBalance() in Token.sol
def get_balance(token_address):
    return contract.functions.getBalance(token_address).call()

# Calls mint() in Token.sol
# Creates a transaction from the call to mint(). Signs the transaction and 
# passes it as a raw transaction to the Ethereum blockchain 
def mint(receiver_address, mint_amount, signature):
    transaction_body = {
        'chainId':3, # 3 is the chainId for Ropsten. Update if using a different chain
        'nonce':get_nonce(receiver_address),
        'gas': 100000,
        'gasPrice': w3.toWei('1', 'gwei'),
    }
    transaction_hash = contract.functions.mint(receiver_address, mint_amount).buildTransaction(transaction_body)
    signed_transaction = w3.eth.account.sign_transaction(transaction_hash, signature)
    result = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

# Calls send() in Token.sol
# Creates a transaction from the call to send(). Signs the transaction and 
# passes it as a raw transaction to the Ethereum blockchain 
def send(sender_address, receiver_address, send_amount, signature):
    transaction_body = {
        'chainId':3, # 3 is the chainId for Ropsten. Update if using a different chain
        'nonce':get_nonce(sender_address),
        'gas': 100000,
        'gasPrice': w3.toWei('1', 'gwei'),
    }
    transaction_hash = contract.functions.send(receiver_address, send_amount).buildTransaction(transaction_body)
    # w3.eth.wait_for_transaction_receipt(transaction_hash)
    signed_transaction = w3.eth.account.sign_transaction(transaction_hash, signature)
    result = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
