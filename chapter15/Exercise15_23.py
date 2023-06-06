# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(String permutation) Write a recursive function to print all the permutations of a
string. For example, for the string abc, the printout is:
    abc
    acb
    bac
    bca
    cab
    cba
(Hint: Define the following two functions. The second function is a helper
function.)

    def displayPermutation(s):
    def displayPermutationHelper(s1, s2):

The first function simply invokes displayPermutation(" ", s). The second
function uses a loop to move a character from s2 to s1 and recursively invokes
it with a new s1 and s2. The base case is that s2 is empty and prints s1 to the
console.
    Write a test program that prompts the user to enter a string and displays all its
permutations.'''


def main():
    # Prompt the user to enter a string
    s = input("Please enter a string: ")

    # Display result
    displayPermutation(s)


# Simply invoke displayPermutation
def displayPermutation(s):
    displayPermutationHelper("", s)


def displayPermutationHelper(s1, s2):
    if len(s2) == 0:
        # Base case: s2 is empty, formed a complete permutation
        print(s1)
    else:
        for i in range(len(s2)):
            # Move character at index i from s2 to s1
            new_s1 = s1 + s2[i]
            new_s2 = s2[:i] + s2[i + 1:]
            # Recursively generate permutations with the updated s1 and s2
            displayPermutationHelper(new_s1, new_s2)


main()
