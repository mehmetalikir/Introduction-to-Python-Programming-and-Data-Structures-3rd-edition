# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Reverse the content of a file) Write a program that will reverse the content of a
text file, so the text will appear back to front. The reversed text should be written
back to the file. Your program should the user to enter a filename. '''


def main():
    # Prompt the user to enter filename
    f1 = input("Enter a filename: ").strip()

    # Open file for input
    inputFile = open(f1, "r")

    fileContent = inputFile.read()  # Read all from the file

    reversedContent = fileContent[::-1]  # Use the slice statement to reverse the text

    inputFile.close()  # Close the input file

    outputFile = open(f1, "w")  # Re-open the same file for writing

    outputFile.write(reversedContent)

    outputFile.close()  # Close the output file


main()
