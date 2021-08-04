// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract Token {
    /*
    * @title A Simple Subcurrency Example
    * @author Jessica Lin
    * @dev This is a demo with inspiration from the Solidity example:
    * https://docs.soliditylang.org/en/stable/introduction-to-smart-contracts.html#subcurrency-example 
    * 
    */

    // The keyword "public" makes variables
    // accessible from other contracts
    address public minter;
    mapping (address => uint) public balances;

    // Events allow clients to react to specific
    // contract changes you declare
    event Sent(address from, address to, uint amount);

    // Constructor code is only run when the contract is created
    constructor() {
        minter = msg.sender;
    }
    
    /// @notice eturns the  an amount of newly created coins to an address
    /// @dev This does not return any value
    /// @param address
    /// @return number of tokens
    function getBalance(address payable _address) public view returns (uint){
        return balances[_address];
    }
    
    /// @notice Mints the given number of tokens and sends to the receiving address. Can only be run by the contract creator
    /// @dev This does not return any value
    /// @param receiver address, amount of tokens to be delivered
    /// @return Nothing
    function mint(address payable receiver, uint amount) public {
        require(msg.sender == minter);
        balances[receiver] += amount;
    }

    /// @notice Errors that notifies the function caller there is an insufficient balance
    error InsufficientBalance(uint requested, uint available);

    /// @notice Sends an amount of existing tokens to a receiving address
    /// @dev This does not return any value
    /// @param receiver address, amount of tokens to be delivered
    /// @return Nothing
    function send(address payable receiver, uint amount) public {
        if (amount > balances[msg.sender])
            revert InsufficientBalance({
                requested: amount,
                available: balances[msg.sender]
            });

        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}
