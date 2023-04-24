# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: hangman) Write a hangman game that randomly generates a word and
prompts the user to guess one letter at a time, as shown in the sample run. Each
letter in the word is displayed as an asterisk. When the user makes a correct
guess, the actual letter is then displayed. When the user finishes a word, display
the number of misses and ask the user whether to continue playing. Create a list
to store the words, as follows:

    # Use any words you wish
    words = ["write", "that", "program", ...]'''
import random


def main():

    guess = input(f"Please enter a letter in word {getAsterisk(getRandomWord())}")


def getAsterisk(word):
    for i in range(0, len(word)):
        word[i] = "*"


def getRandomWord():
    # Use any words you wish
    words = ["write", "that", "program", "carlton", "blackpink"]
    r = str(words[random.randint(0, len(words) - 1)])
    word = [x for x in r]

    return word


main()

# TO-DO > To be continue...
