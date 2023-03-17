# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Student major and status) Write a program that prompts the user to enter two
characters and displays the major and status represented in the characters. The first
character indicates the major and the second is number character 1, 2, 3, 4, which
indicates whether a student is a freshman, sophomore, junior, or senior. Suppose
the following characters are used to denote the majors:
M: Mathematics
C: Computer Science
I: Information Technology'''

# Prompt the user to enter two characters
c = str(input("Please enter two characters: ")).upper()

major = ''
status = ''

if c.startswith('M'):
    major = "Mathematics"
if c.startswith('C'):
    major = "Computer Science"
if c.startswith('I'):
    major = "Information Technology"
if c.endswith('1'):
    status = "Freshman"
if c.endswith('2'):
    status = "Sophomore"
if c.endswith('3'):
    status = "Junior"
if c.endswith('4'):
    status = "Senior"

print("",major,"\n",status)