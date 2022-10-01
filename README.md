# BankingSystem (Read the last section before running the code)

## Why this project and what does it do?

This project was done in my high school (Jan 2021) as an opportunity for me to put my Python and MySQL skills to use.

The purpose of this project is to showcase the working of a Banking system which users can:
- create a bank account 
- deposit money in the account 
- withdraw money from the account 
- transfer money from one account to another 
- view their account details 
- view their transaction details 
- change account password
- terminate their account

It automatically records the transactions done by storing the type of transaction, the date of transaction, the amount transacted and the balance after transaction in the form of an invoice.
This reduces the discrepancy of manually keeping track each of the transactions made.

The program makes use of two separate tables which are:
- acc (short for account)
- transac (short for transaction)

## Technical Specifications and User Stories

For detailed specifications of each process and components in the program, kindly refer to [FinalProjectJim.pdf](FinalProjectJim.pdf)

## Before Running the Code

1. Make sure mySQL and mySQLConnector is installed and running.
2. Make sure that the parameter values (i.e.: host, user, password) are correct.
3. Run the scripts in MySqlScripts.txt

Helpful Resources:

[MySQLConnector for bash](https://www.youtube.com/watch?v=UcpHkYfWarM)

[MySQLConnector for zsh](https://www.youtube.com/watch?v=oxToe-4c6OM)
