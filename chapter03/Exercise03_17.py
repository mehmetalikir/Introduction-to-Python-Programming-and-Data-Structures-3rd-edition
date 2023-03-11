# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-paper
game. (Scissors can cut a paper, a rock can knock scissors, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.'''

import random

# Generate number for computer
computer = random.randint(0, 2)

# Prompt the user to enter a number 0, 1, 2
user = int(input("Please select an option -> Scissor (0), rock (1), paper (2): "))

# Check who win and display result
match computer:
    case 0:
        str = "The computer is scissor"
        if user == 0:
            print(str, ", You are scissor too. It is a draw")
        elif user == 1:
            print(str, ", You are rock. Congratulations , You won! ")
        else:
            print(str, ", You are paper. Sorry, You lost the game")
    case 1:
        str = "The computer is rock"
        if user == 1:
            print(str, ", You are rock too. It is a draw")
        elif user == 2:
            print(str, ", You are paper. Congratulations , You won! ")
        else:
            print(str, ", You are scissor. Sorry, You lost the game")

    case 2:
        str = "The computer is paper"
        if user == 2:
            print(str, ", You are paper too. It is a draw")
        elif user == 0:
            print(str, ", You are scissor. Congratulations , You won! ")
        else:
            print(str, ", You are rock. Sorry, You lost the game")
