# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Convert milliseconds to hours, minutes, and seconds) Write a function that converts
milliseconds to hours, minutes, and seconds using the following header:

    def convertMillis(millis):

The function returns a string as hours:minutes:seconds. For example,
convertMillis(5500) returns a string 0:0:5, convertMillis(100000) returns
a string 0:1:40, and convertMillis(555550000) returns a string 154:19:10.
    Write a test program that prompts the user to enter a value for milliseconds
and displays a string in the format of hours:minutes:seconds'''


def convertMillis(millis):

    hours = millis // 3600000
    minutes = millis // 60000
    minutes %= 60
    seconds = millis // 1000
    seconds %= 60

    print(hours,":",minutes,":",seconds)


def main():
    # Prompt the user to enter a value for milliseconds
    millis = int(input("Please enter in milliseconds: "))

    # Display result
    convertMillis(millis)


main()
