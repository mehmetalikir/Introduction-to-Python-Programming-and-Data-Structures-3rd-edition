# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Display pattern) Write a function to display a pattern a follows:
1
2 1
3 2 1
4 3 2 1
...
The function header is


Write a test program that prompts the user to enter a number n and invokes
displayPattern(n) to display the pattern'''
def displayPattern(n):

    # Print triangle pattern
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print('')

def main():

    # Prompt the user to enter a number n
    n = int(input("Please enter line number: "))

    displayPattern(n) # Invoke function

main()


