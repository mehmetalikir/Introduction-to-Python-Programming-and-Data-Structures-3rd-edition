# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display nonduplicate words in ascending order) Write a program that prompts
the user to enter a text file, reads words from the file, and displays all the nonduplicate
words in ascending order.'''

def main():
    # Prompt the user to enter filenames
    f1 = input("Please enter a filename: ").strip()

    # Open files for input
    inputFile = open(f1, "r")

    s = inputFile.read()  # Read all from the file
    inputFile.close()

    words = s.split()
    nonduplicateWords = set(words)
    words = list(nonduplicateWords)
    words.sort(reverse=True)

    for word in words:
        print(word, end=" ")


main()
