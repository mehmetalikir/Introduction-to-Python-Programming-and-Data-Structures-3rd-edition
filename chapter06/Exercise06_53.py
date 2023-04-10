# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Occurrences of a specified character) Write a function that fins the number of
occurrences of a specified character in the string using the following header:

def count(s, ch):

For example, count ("Welcome", 'e') returns 2. The str class has the count
 method(function). Implement your method(function) without using the count method. Write a
 test program that reads a string and a character and displays the number of occurrences
 of the character in the string.'''


def main():
    # Prompt the user to enter a string and a character
    s = input("Please enter a string: ")
    ch = input("Please enter a character: ")

    # Display result
    print(f"{ch} appears in {s}{count(s, ch)} times")

    # Compare result
    print("Return of the str class's function: ", s.count(ch))


def count(s, ch):
    # Assign value
    count = 0

    # Get the number of occurrences of the character in the string
    for i in range(0, len(s), +1):
        if s[i] == ch:
            count += 1

    return count


main()  # Call main function
