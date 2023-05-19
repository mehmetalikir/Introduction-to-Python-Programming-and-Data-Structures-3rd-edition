# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Encrypt files) Encode the file by adding 2 to every byte in the file. Write a program
that prompts the user to enter an input filename and an output filename and
saves the encrypted version of the input file to the output file.'''


def main():
    f1 = input("Please enter a source filename: ").strip()
    f2 = input("Please enter a target filename: ").strip()

    # Open file for input
    inputFile = open(f1, "r")

    s = inputFile.read()  # Read all from the file

    newS = ""

    for i in range(len(s)):
        newS += chr(ord(s[i]) + 2)

    inputFile.close()  # Close the input file
    outputFile = open(f2, "w")

    print(newS, file=outputFile, end="")  # Write to the file
    print("Done")

    outputFile.close()  # Close the output file


main()

