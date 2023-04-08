# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compute the probability) Use the functions in RandomCharacter in Listing
6.10 to generate 10_000 uppercase letters and count the occurrence of letter A.'''

import RandomCharacter


def main():
    # Constant
    NUMBER_OF_CHARS = 10_000  # Number of characters to generate
    CHARS_PER_LINE = 50  # Numbers of characters to display per line

    # Assign value
    count = 0

    # Print random characters between 'a' and 'z', 50 chars per line
    for i in range(NUMBER_OF_CHARS):
        print(RandomCharacter.getRandomUpperCaseLetter(), end="")
        if RandomCharacter.getRandomUpperCaseLetter() == 'A':
            count += 1
        if (i + 1) % CHARS_PER_LINE == 0:
            print()  # Jump to the new line

    print("__________________________________________________")
    print(f"The occurrence of letter A is {count} in {NUMBER_OF_CHARS}")


main()  # Call the main function
