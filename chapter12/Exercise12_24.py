# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Extend the str class) Define the MyString class to extend the str class with
the following new method.'''

class MyString(str):

    def __new__(cls, s=""):
        return str.__new__(cls, s)

    # Return true if s string is found within
    # this string irrespective of case
    def isFoundIgnoreCase(self, s):
        return s.upper() in self.upper()


def main():
    s1 = input("Enter string s1: ")
    s2 = input("Enter string s2: ")

    print(MyString(s1).isFoundIgnoreCase(s2))

main()

