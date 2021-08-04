"""
User entry-point into the app
"""
import inquirer
from demo_token import *

print("Welcome to the Demo Token App")

# Prompt the user for an action
# Uses inqurier, an interactive command line user interface
question = [
  inquirer.List('action',
                message="What would you like to do?",
                choices=['Mint A Token', 'Get Token Balance', 'Send Tokens'],
            ),
]
answer = inquirer.prompt(question)['action']

# Option - Get Token Balance
# Takes in an ETH address and queries get_balance() from token.py
if answer == 'Get Token Balance':
    print("Getting Token Balance")
    question = [
        inquirer.Text('address',
                    message="Enter an ETH address: "),
    ]
    token_address = inquirer.prompt(question)['address']
    print(get_balance(token_address))

# Option - Mint Token
# Sends an amount of newly created tokens to an address using mint() from token.py
# Will only work if called by the contract creator
elif answer == 'Mint A Token':
    print("Minting A Token \n(Note: Only the account that deployed the smart contract can mint tokens)")
    questions = [
        inquirer.Text('amount',
                    message="Enter the amount of tokens to mint"),
        inquirer.Text('receiver_address',
                    message="Who would you like to give the tokens to (enter an ETH address)?"),
        inquirer.Text('signature',
                    message="Enter the minter's private key"),
    ]   
    answers = inquirer.prompt(questions)
    mint(answers['receiver_address'], int(answers['amount']), answers['signature'])

# Option - Send Tokens
# Sends an amount of existing created tokens from any caller to any receiver using send() from token.py
elif answer == 'Send Tokens':
    print("Sending Tokens")
    questions = [
        inquirer.Text('sender_address',
                    message="Enter the sender's ETH address"),
        inquirer.Text('receiver_address',
                    message="Enter the receiver's ETH address"),
        inquirer.Text('send_amount',
                    message="Enter the amount of Tokens to send"),
        inquirer.Text('signature',
                    message="Enter the sender's private key"),
    ] 
    answers = inquirer.prompt(questions)
    send(answers['sender_address'], answers['receiver_address'], int(answers['send_amount']), answers['signature'])
