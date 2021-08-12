# Ankr Demo - Mint and Send Tokens

## Table of Contents

* [Overview](#overview)
  * [Motivation and Target Audience](#motivation-and-target-audience) 
* [Installation Requirements](#installation-requirements)
* [How To Use](#how-to-use)
  * [Step 1. Connect to the Ethereum blockchain using Ankr](#step-1.-connect-to-the-ethereum-blockchain-using-ankr)
  * [Step 2. Compile a Smart Contract using MetaMask and Remix](#step-2.-compile-a-smart-contract-using-metamask-and-remix)
  * [Step 3. Interact with Smart Contract Using Python](#step-3.-interact-with-smart-contract-using-python)
* [Resources](#resources)
* [Common Errors](#common-errors)


## Overview

This is a simple python app that interacts with the Ethereum blockchain through [Web3.py](https://web3py.readthedocs.io/en/stable/), an [Ankr API endpoint](https://www.ankr.com/), and a [Solidity](https://docs.soliditylang.org/en/stable/) smart contract. Users can interact with the app through the command line (CLI).

<img src="https://drive.google.com/uc?export=view&id=1pGJD71PCc5POlR-FXHAmsLSglXSK4Gir" alt="Diagram" width="500"/>

This app creates a simple, non-ERC20 token (based off of the [Solidity example](https://docs.soliditylang.org/en/v0.8.6/introduction-to-smart-contracts.html#subcurrency-example)). The contract allows only its creator to create new tokens; however, anyone can send tokens to each other. Anyone can also read the token balance from a given address. 

Below is a screenshot of the CLI-based UI from which users can choose from one of three tasks - Mint Tokens, Get Token Balance, Send Tokens - all using Ethereum addresses. 

<img src="https://drive.google.com/uc?export=view&id=1Hpo01h5jMXIVUUcZQmjGgYku-JQ7FbYO" alt="CLI screenshot" width="500"/>

#### Motivation and Target Audience
This project is intended for developers with a basic familiarity with concepts such as - blockchain, smart contract, and web3 API endpoints. It also assumes a basic familiarity with tools such as - Python, Web3.py, MetaMask, and Remix. It aims to provide a cohesive example of a Python app that queries and writes to the Ethereum blockchain. This project is not meant to be production-ready and is intended to purely be an example. 

## Installation Requirements
-   Python 3
-   Install virtualenv: `pip3 install virtualenv`
-   Install requirements inside the virutalenv you've created (ex: demoenv):
     ```
     cd AnkrDemo
     source demoenv/bin/activate
     pip3 install -r requirements.txt
     ```
     
## How To Use

### Step 1. Connect to the Ethereum blockchain using Ankr
To start, you need to connect to the Ethereum blockchain. There are different ways to do this (e.g. locally via Ganache), in this example I will connect to a live blockchain using [Ankr](https://docs.ankr.com/).
 
* Signup for an [Ankr account](https://app.ankr.com/auth/sign-up).
* From API Market, select to deploy the "Ethereum Full" option: 

<img src="https://drive.google.com/uc?export=view&id=1FzTlZrhlj6kEtHQv_37XOJcq20dCzaPL" alt="Ankr API Market" width="500"/>

* Select one of the testnet options if you are in the free tier (I chose Ropsten because I could easily get free ETH from a faucet): 

<img src="https://drive.google.com/uc?export=view&id=1Y2oCt9osf3ZdIdhw4AtDD8j64SlwZnJ1" alt="Testnest option" width="500"/>

* Select either the Basic authentication or Token method. In my example, I use the Token method which does not require a Project username and password. If you use the Basic authentication method, make sure to format the Web3 HTTPProvider call properly as [discussed here](https://stackoverflow.com/a/68646478/16590504).

<img src="https://drive.google.com/uc?export=view&id=1Y2oCt9osf3ZdIdhw4AtDD8j64SlwZnJ1" alt="Token method" width="500"/>

* Copy the API Endpoint and paste into `.env` as the value of `NODE_PROVIDER`.


### Step 2. Compile a Smart Contract using MetaMask and Remix
Next, you will need to compile and deploy the smart contract. There are a number of ways to do this, in this example we will use [Remix](https://remix.ethereum.org/) and [MetaMask](https://metamask.io/).

* Install [MetaMask](https://metamask.io/) and create an account. This is a browser extension that will allow you to interact with the Ethereum blockchain through your browser. 
* Fund your MetaMask account with ETH from a faucet such as [this Ropsten faucet](https://metamask.io/).
* Open `Token.sol` in [Remix](https://remix.ethereum.org/). Compile the smart contract. Deploy it using the "Injected Web3" environment which will use funds from your MetaMask account. 
* Copy the contract's ABI, bytecode, and contract address and paste into the `.env` file as the values of `CONTRACT_ABI`, `CONTRACT_BYTECODE`, `CONTRACT_ADDRESS` respectively.

### Step 3. Interact with Smart Contract Using Python
Now we can interact with the app. Fire up the app by running the `main.py` Python script in your terminal and start minting and sharing your tokenw!
* From the virtualenv in a CLI, run `python3 main.py`
 * From the prompts, choose from one of the 3 options:
	 * **Mint Tokens** - A specified number of tokens are minted and sent to the recipient's address. User enters the number of tokens to mint and an ETH address that will receive these tokens (Note: Only the account that deployed the smart contract can mint tokens; however, anyone can receive the token. The minter's private key is required to complete this transaction). 
	 * **Get Token Balance** - Returns the token balance from a given ETH address. 
	 * **Send Tokens** - Sends tokens from one address to another. User enters the sender and receiver's ETH addresses, the number of tokens to be sent, and the sender's private key (Note: The balances may not immediately update because the transactions may take a while to be added to the blockchain).

<img src="https://drive.google.com/uc?export=view&id=1g5I5tDGP3ATAQhE8Vrb35yZhxeLUwzre" alt="Running script in terminal" width="1000"/>


## Resources
* [Web3.py](https://web3py.readthedocs.io/en/stable/) - a Python library for interacting with Ethereum
* [How to format Ankr API call when using Python Web3 HTTPProvider ](https://stackoverflow.com/a/68646478/16590504)
* [Subcurrencey Solidity Smart Contract Example](https://docs.soliditylang.org/en/v0.8.6/introduction-to-smart-contracts.html#subcurrency-example)

### Common Errors
* If you receive *ValueError: {'code': -32000, 'message': 'only replay-protected (EIP-155) transactions allowed over RPC'}*, make sure to add chainId in transaction body [(Source)](https://ethereum.stackexchange.com/questions/94412/valueerror-code-32000-message-only-replay-protected-eip-155-transac).
* If you receive *ValueError: {'code': -32000, 'message': 'already known'}*, the transaction is still processing.  Wait a bit and try again. 
* If you recieve *ValueError: {'code': -32000, 'message': 'nonce too low'}*, the transaction is still processing. Wait a bit and try again. 
* If after you send tokens to an address and the balance is does not update, it may be that the transactions have not been added to the blockchain yet. Either check the status of the transaction hash (retreive from `demo_token.py`) or give it some time. 

