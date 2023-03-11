# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: lottery) Revise Listing 3.8, Lottery.java, to generate a lottery of a threedigit
number. The program prompts the user to enter a three-digit number and
determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
2. If all digits in the user input match all digits in the lottery number, the
award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award
is $1,000.'''

import random

# Generate a lottery
lottery = random.randint(0, 99)

# Prompt the user to enter a guess
guess = int(input("Please enter your lottery pick (two digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits form guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: You win $10,000")
elif (guessDigit2 == lotteryDigit1
      and guessDigit1 == lotteryDigit2):
    print("Match all digits: You win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit; You win $1,000")
else:
    print("Sorry, no match")
