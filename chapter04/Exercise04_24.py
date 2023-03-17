# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Vowel or consonant?) Assume letters A/a, E/e, I/i, O/o, and U/u as the vowels.
Write a program that prompts the user to enter a letter and check whether the
letter is a vowel or consonant.'''

# Prompt the user to enter a letter
c = (str(input("Please enter a letter (A-Z or a-z): ")))

# Convert the letter to uppercase
c = c.upper()

# Display result
if 'A' <= c <= 'Z':
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        print(f"{c} is a vowel")
    else:
        print(f"{c} is a consonant")
else:
    print("Please enter valid letter")
