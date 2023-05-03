# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Account class) Design a class named Account that contains:

    ■ A private int data field named id for the account.
    ■ A private float data field named balance for the account.
    ■ A private float data field named annualInterestRate that stores the current
    interest rate.
    ■ A constructor that creates an account with the specified id (default 0), initial
    balance (default 100), and annual interest rate (default 0).
    ■ The accessor and mutator functions for id, balance, and annualInterestRate.
    ■ A function named getAnnualInterestRate() that returns the annual
    interest rate.
    ■ A function named getAnnualInterest() that returns the annual interest.
    ■ A function named withdraw that withdraws a specified amount from the
    account.
    ■ A function named deposit that deposits a specified amount to the account.

Draw the UML diagram for the class, and then implement the class. (Hint: The
function getAnnualInterest() is to return the annual interest amount, not
the interest rate. Use this formula to calculate the annual interest: balance *
annualInterestRate. annualInterestRate is annualInterestRate. Note that
annualInterestRate is a percent (like 0.375%). You need to divide it by 100.)
    Write a test program that creates an Account object with an account id of 1122, a
balance of $20,000, and an annual interest rate of 0.375%. Use the withdraw
function to withdraw $2,500, use the deposit function to deposit $3,000, and print
the id, balance, monthly interest rate, and monthly interest.'''


class Account:
    # Construct an Account object
    def __init__(self, id=0, balance=100, annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    # The accessor and mutator functions
    def getId(self):
        return self.__id

    def setId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def setBalance(self):
        return self.__balance

    # Return the annual interest rate
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self):
        return self.__annualInterestRate

    # Return the annual interest
    def getAnnualInterest(self):
        return self.__balance * self.getAnnualInterestRate() / 100

    # A function named withdraw that withdraws a specified amount from the account
    def withdraw(self, amount):
        self.__balance -= amount

    # A function named withdraw that withdraws a specified amount from the account
    def deposit(self, amount):
        self.__balance += amount


def main():
    # Create a Petroleum's product
    account1 = Account(1122, 20_000, 0.375)
    account1.withdraw(2_500)
    account1.deposit(3_000)
    print(f"The account' id: {account1.getId()},balance: ${account1.setBalance()}, "
          f"annual interest: ${account1.getAnnualInterest()}")


main()  # Call the main function
