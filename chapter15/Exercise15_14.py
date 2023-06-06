# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrences of a specified character in a string) Rewrite Exercise 15.10 using a
helper function to pass the substring of the high index to the function. The
helper function header is:

    def countHelper(s, a, high):

'''


def main():
    # Prompt the user to enter a string and a character
    s = input("Please enter a string: ").strip()
    ch = input("Please enter a character: ")[0]

    times = count(s, ch)

    # Display the number of times the character occurs in the string
    print(ch + " appears " + str(times) + (" times " if times > 1 else " time ") + "in " + s)


# Count the number of occurrences of a specified character in a string
def count(s, a):
    return countHelper(s, a, len(s) - 1)


# Helper function used to pass the substring high index
def countHelper(s, a, high):
    result = 0
    if high >= 0:  # Base case
        result = countHelper(s, a, high - 1) + (1 if s[high] == a else 0)  # Recursive call

    return result


main()
