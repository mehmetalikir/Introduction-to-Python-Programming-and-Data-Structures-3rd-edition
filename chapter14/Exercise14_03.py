# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create dictionary of words by initial) Write a program that reads the content of
a text file and store each word in a dictionary based on its initial. For instance,
all words starting with 'a'. The initial (string) will be the key and the value will
be a set. After allocating the words from
the file to the dictionary, the program should print the contents of the dictionary
sorted alphabetically. Your program should prompt the user to enter a filename: to
read. Duplicated words should only be included once. An example output cloud be:'''


def main():
    filename = input("Please enter the filename to read: ")
    wordDictionary = createWordDictionary(filename)
    printSortedDictionary(wordDictionary)


def createWordDictionary(filename):
    # Create an empty dictionary
    wordDict = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                initial = word[0]  # Get the initial letter
                if initial not in wordDict:
                    wordDict[initial] = set()  # Create an empty set for the initial letter
                wordDict[initial].add(word)  # Add the word to the set

    return wordDict


def printSortedDictionary(wordDict):
    for initial, words in sorted(wordDict.items()):
        sortedWords = sorted(words)
        print(f"{initial} \n"
              f"    {sortedWords}\n")


main()
