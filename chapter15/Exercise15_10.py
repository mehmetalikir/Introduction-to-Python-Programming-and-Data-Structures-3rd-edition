# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrences of a specified word in a text file) Write a  program using a
recursive function that finds the number of occurrences of a specified word in a text file
using the following function header:

    def countWords(words, word, count):

This function should take in a list of words, the word to find, and the current
count value.
    The program should prompt the user to enter a text file name, a word, and
display the number of occurrences of the word in the file.'''


def main():
    # Prompt the user to enter a text file name, a word
    filename = input("Please enter a filename: ")
    word = input("Please enter a word: ")

    inputFile = open(filename, "r")
    s = inputFile.read()
    inputFile.close()

    words = s.split()

    count = countWords(words, word, 0)

    # Display the number of occurrences
    print(f"{word} appears {count} {'time' if count == 1 else 'times'} in the file")


# Find the number of occurrences of a specified word in a text file
def countWords(words, word, count):
    if words:
        if words[0] == word:  # Base case
            count += 1
        words.pop(0)
        count = countWords(words, word, count)  # Recursive call
    return count


main()
