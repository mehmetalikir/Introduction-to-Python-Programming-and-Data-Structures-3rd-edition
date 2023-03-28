# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Count vowels and consonants) Assume letters A, E, I, O, and U as the vowels.
Write a program that prompts the user to enter a string and displays the number
of vowels and consonants in the string.'''

# Constant
vowels = "AEIOU"

# Prompt the user to enter a string
s = input("Please enter a string: ").upper()

# Assign values
vowelsCount, consonantsCount, c = 0, 0, ''

# Count the number of vowels and consonants
for i in range(0,len(s)):
    c = s[i]
    if c.isalpha():
        if vowels.__contains__(c):
            vowelsCount += 1
        else:
            consonantsCount += 1

print("The number of Vowel is ", vowelsCount)
print("The number of consonants is ",consonantsCount)