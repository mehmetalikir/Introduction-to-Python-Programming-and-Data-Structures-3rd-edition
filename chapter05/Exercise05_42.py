# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Process string) Write a program that prompts the user to enter a string and displays
the all the characters at positions 3, 6, 9 and so on'''

# Prompt the user to enter a string
s1 = input("Please enter a string: ")

# Assign values
position = 2
s2 = ""

for i in range(0,len(s1), +3):
    s2 += s1[position]
    position += 3

# Display result
print(s2)


