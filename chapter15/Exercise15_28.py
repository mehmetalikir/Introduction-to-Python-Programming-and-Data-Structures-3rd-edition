# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find words) Write a program that finds all the occurrences of a word in all the
files under a directory, recursively. Your program should prompt the user to enter
a directory name.'''

import os


def main():
    # Prompt the user enter a directory name
    path = input("Please enter a directory or a file: ").strip()
    s = input("Please enter a string: ").strip()

    # Display the size
    try:
        findinput(path, s)
    except:
        print("File or directory does not exist")


def findinput(path, word):
    try:
        if not os.path.isfile(path):
            list = os.listdir(path)  # All files and subdirectories
            for i in range(len(list)):
                findinput(list[i], word)  # Recursive call
        else:  # Base case
            findWord(path, word)
    except:
        print("Let it go")


def findWord(file, word):
    try:
        inputFile = open(file, "r")
        for line in inputFile:
            if line.find(word) > -1:
                print(file + ": " + line)
    except:
        print("Let is go")
    finally:
        inputFile.close()


main()
