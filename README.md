# python-oop-bank-system
A simple bank account simulation built with Object-Oriented Programming.
## Features

- Create bank accounts
- Deposit funds
- Withdraw funds
- Transfer funds between accounts
- Balance validation
- Custom object representation using __repr__

## OOP Concepts Demonstrated

- Classes
- Objects
- Constructors (__init__)
- Instance Attributes
- Instance Methods
- Encapsulation
- Object-to-Object Interaction

## Example

acct_1 = Bank("Janet", 1111)
acct_2 = Bank("John", 2222)

acct_1.deposit(500)
acct_1.transfer(acct_2, 1000)
