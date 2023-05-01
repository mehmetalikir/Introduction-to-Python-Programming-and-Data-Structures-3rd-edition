# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Identical lists) The two-dimensional lists m1 and m2 are identical if they have the
same contents. Write a function that returns True if m1 and m2 are identical, using
the following header:

    def equals(m1, m2):

Write a test program that prompts the user to enter two 3 x 3 lists of
integers and displays whether the two are identical.'''


def main():
    m1 = input("Please enter list1: ").split()  # 51 22 25 6 1 4 24 54 6
    m2 = input("Please enter lisst2: ").split()  # 51 22 25 6 1 4 24 54 6

    if equals(m1, m2):
        print("Two lists are identical")
    else:
        print("Two lists are not identical")


def equals(m1, m2):
    for i in range(len(m1)):
        if int(m2[i]) != int(m1[i]):
            return False

    return True


main()  # Invoke main function
