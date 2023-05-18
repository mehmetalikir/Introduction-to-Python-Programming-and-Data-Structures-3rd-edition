# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Reading, writing and appending to file) Write a program that prompts the user
for a file name. If the file exists, open it and print it its content back to user.
If it does not exist, create the file. The user should then be prompted to repeatedly
enter text which is added to the file. The program should exit when the user
writes END'''
import os.path


def main():
    # Check whether file is exist or not
    if os.path.isfile("test.txt"):
        print("test.txt exists")

    # Open file for input
    inputFile = open("test.txt", "r")
    print(inputFile.read())

    # Open file for output
    # outputFile = open("test.txt", "w")
    # # Write data the file
    # outputFile.write("Text1\n")
    # outputFile.write("Text2\n")

    # Open file for appending data
    outputFile = open("test.txt", "a")

    while True:
        s1 = input("PLease enter text to write to file (type END when you are done): ")
        if s1 == "END":
            break
        outputFile.write(f"{s1}\n")

    print(inputFile.read())
    inputFile.close()  # Close the input file


main()
