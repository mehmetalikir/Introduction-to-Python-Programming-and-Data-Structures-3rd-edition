# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Game: locker puzzle) A school has 100 lockers and 100 students. All lockers are
closed on the first day of school. As the students enter, the first student, denoted
S1, opens every locker. Then the second student, S2, begins with the second
locker, denoted L2, and closes every other locker. Student S3 begins with the
third locker and changes every third locker (closes it if it was open, and opens it if
it was closed). Student S4 begins with locker L4 and changes every fourth locker.
Student S5 starts with L5 and changes every fifth locker, and so on, until student
S100 changes L100.
After all the students have passed through the building and changed the lockers,
which lockers are open? Write a program to find your answer and display all
open locker numbers separated by exactly one space.
(Hint: Use a list
 of 100 Boolean elements, each of which indicates whether a
locker is open (true) or closed (false). Initially, all lockers are closed.)'''



def main():
    # Create a list
    lst = createList()

    # Display result
    displayResult(lst)

# Create a list of 100 Boolean elements
def createList():
    # Initially, all lockers are closed
    lockers = 100 * [False]

    for s in range(1, len(lockers)):
        for l in range(0, len(lockers)):
            if l % s == 0:
                lockers[l] = not lockers[l]

    return lockers

# Display all open locker numbers separated by exactly one space
def displayResult(lockers):
    for i in range(0, len(lockers)):
        if lockers[i]:
            print(f"L{i + 1} ")


main() # Invoke main function
