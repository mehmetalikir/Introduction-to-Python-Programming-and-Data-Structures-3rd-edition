# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Replace text) Write a program that replaces text in a file. Your program should
prompt the user to enter a filename, an old string, and a new string.'''


def main():
    # Prompt the user to enter filename
    f1 = input("Enter a filename: ").strip()

    # Read input file
    inputFile = open(f1, "r")

    s1 = input("Please enter the old string to be replaced:")
    s2 = input(("Please enter the new string to replace the old string: "))

    # Read all from the file
    s = inputFile.read()

    # Replace old string
    s = s.replace(s1, s2)

    # Close input file
    inputFile.close()

    # Open input file again to re-write
    outputFile = open(f1, "w")

    # Override the input file with the new string
    outputFile.write(s)

    # Close input file
    outputFile.close()


main()
