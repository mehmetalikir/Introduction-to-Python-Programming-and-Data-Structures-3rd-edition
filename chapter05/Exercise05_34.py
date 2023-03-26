# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: lottery) Revise Listing 3.9, Lottery.py, to generate a lottery of a two-digit
number. The two digits in the number are distinct. (Hint: Generate the first
digit. Use a loop to continuously generate the second digit until it is different
from the first digit.)'''


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
