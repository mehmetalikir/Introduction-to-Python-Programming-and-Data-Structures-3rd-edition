# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: ATM) Use the Account class created in Exercise 7.3 to simulate
an ATM. Create ten accounts in a list with the ids 0, 1, ..., 9, and an initial
balance of $100. The system prompts the user to enter an id. If the id is entered
incorrectly, ask the user to enter a correct id. Once an id is accepted, the main
menu is displayed as shown in the sample run. You can enter a choice of 1 for
viewing the current balance, 2 for withdrawing money, 3 for depositing money,
and 4 for exiting the main menu. Once you exit, the system will prompt for an id
again. So, once the system starts, it won’t stop.'''
import sys

from chapter12.Acccount import Account

ac = Account(0, 0.0)  # Set default account

for i in range(10):  # Set 10 accounts
    ac.setId(i)
    ac.setBalance(100)  # Set initial balance of $100

id = int(input("Please enter an id:"))

while True:
    menu = int(input("Main menu\n"
                     "1: check blance\n"
                     "2: withdrawn\n"
                     "3: deposit\n"
                     "4: exit\n"
                     "Please enter a choice:"))

    match menu:
        case 1:
            print("The balance is", ac.getBalance(id))
            continue
        case 2:
            amount = float(input("Please enter an amount to withdraw: "))
            ac.withdraw(amount)
            continue
        case 3:
            amount = float(input("Please enter an amount to deposit: "))
            ac.deposit(amount)
            continue
        case 4:
            sys.exit(0)
