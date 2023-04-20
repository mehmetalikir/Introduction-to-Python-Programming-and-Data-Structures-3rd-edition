# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Anagrams) Write a function that checks whether two words are anagrams. Two
words are anagrams if they contain the same letters. For example, silent and
listen are anagrams. The header of the function is:

    def isAnagram(s1, s2)

(Hint: Obtain two lists for the two stings. Sort the lists and check if two lists are
identical.) Write a test program that prompts the user to enter two stings and
checks whether they are anagrams'''


def main():
    # Prompt the user to enter strings
    s1 = input("Please enter the first string: ")
    s2 = input("Please enter the second string: ")


    # Display result
    displayResult(s1, s2)


def createList(s):
    # Create empty list
    lst = []

    # Obtain  list for the sting
    for i in range(len(s) - 1):
        lst += s[i]

    # Sort the lists.
    lst.sort()

    # Return the list
    return lst


# Display result
def displayResult(s1, s2):
    # Create a list
    list1 = createList(s1)
    list2 = createList(s2)

    if isAnagram(list1,list2):
        print(f"{s1} and {s2} are anagrams")
    else:
        print(f"{s1} and {s2} are not anagrams")


# Check if strings are substrings of each other
def isAnagram(s1, s2):
    if len(s1) > len(s2):
        s1 = s2

    for i in range(len(s2) - 1):
        if s1[i] == s2[i]:
            return True
        else:
            return False


main()  # Call main function
