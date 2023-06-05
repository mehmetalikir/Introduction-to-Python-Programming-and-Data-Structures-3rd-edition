# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the longest word in a list) Write a recursive function that returns the
longest string in a list. Write a main program that prompts the user to enter a string
of words and displays the longest word.'''


def findLongestWord(words):
    if len(words) == 1:  # Base case
        return words[0]
    else:
        firstWord = words[0]
        restWords = words[1:]
        longestRest = findLongestWord(restWords)  # Recursive call

        if len(firstWord) > len(longestRest):
            return firstWord
        else:
            return longestRest


def main():
    # Prompt the user to enter a string
    s = input("Please enter a string: ")
    wordList = s.split()

    longestWord = findLongestWord(wordList)

    # Display result
    print(f"The longest word in {wordList} is {longestWord}")


main()
