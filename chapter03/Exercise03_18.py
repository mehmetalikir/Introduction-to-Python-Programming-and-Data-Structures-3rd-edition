# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Travel app: fare calculation) Write a program that prompts the user to enter the
fare of 1km. Prompt the user to enter 0 to find km traveled for a given amount and
1 to find the fare needed for travelling the given km. For 0, prompt the user to enter
the amount in dollars and display how many kms can be travelled, and for 1 prompt
the user to enter the kms and display how many are needed to travel.'''

# Prompt the user to enter the fare of 1km
cost = float(input("Please enter per km fare in dollar: "))

# Prompt the user to enter 0 or 1
option = int(input("Please enter 0 to find KMs travel for an amount and 1 for vice versa: "))

# Calculate and display result
if option == 0:
    amount = float(input("Please enter the amount in dollars: "))
    print(format(amount, ".2f"), "dollars provide a travel of", format(amount / cost, ".2f"), "KMs")
else:
    distance = float(input("Please enter the distance in KMs: "))
    print(format(distance, ".2f"), "KMs travel needs an amount of", format(distance * cost, ".2f"), "dollars")
