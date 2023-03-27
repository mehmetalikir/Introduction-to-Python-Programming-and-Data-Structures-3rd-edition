# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: scissor, rock, paper) Programming Exercise 3.17 gives a program that
plays the scissor-rock-paper game. Revise the program to let the user continuously
play until either the user or the computer wins more than two times than its
opponent.'''


import random

# Assign values
userCount = 0
compCount = 0

# Check who win and display result
while userCount < 2 and compCount < 2:

    # Generate number for computer
    computer = random.randint(0, 2)

    # Prompt the user to enter a number 0, 1, 2
    user = int(input("Please select an option -> Scissor (0), rock (1), paper (2): "))
    match computer:
        case 0:
                s = "The computer is scissor"
                if user == 0:
                    print(s, ", You are scissor too. It is a draw")
                elif user == 1:
                    print(s, ", You are rock. Congratulations , You won! ")
                    userCount += 1
                else:
                    print(s, ", You are paper. Sorry, You lost the game")
                    compCount += 1
        case 1:
                s = "The computer is rock"
                if user == 1:
                    print(s, ", You are rock too. It is a draw")
                elif user == 2:
                    print(s, ", You are paper. Congratulations , You won! ")
                    userCount += 1
                else:
                    print(s, ", You are scissor. Sorry, You lost the game")
                    compCount += 1

        case 2:
                s = "The computer is paper"
                if user == 2:
                    print(s, ", You are paper too. It is a draw")
                elif user == 0:
                    print(s, ", You are scissor. Congratulations , You won! ")
                    userCount += 1
                else:
                    print(s, ", You are rock. Sorry, You lost the game")
                    compCount += 1

# Display result
print("Computer: ", compCount, "and User: ", userCount)