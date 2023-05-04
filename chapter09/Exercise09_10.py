# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Time class) Design a class named Time. The class contains:

    ■ The private data fields hour, minute, and second that represent a time.
    ■ A constructor that constructs a Time object that initializes hour, minute, and
    second using the current time.
    ■ The getter methods for the data fields hour, minute, and second, respectively.
    ■ A method named setTime(elapseTime) that sets a new time for the object
    using the elapsed time in seconds. For example, if the elapsed time is 555550
    seconds, the hour is 10, the minute is 19, and the second is 12.

Draw the UML diagram for the class, and then implement the class. Write a test
program that creates a Time object for the current and displays its hour, minute, and second.
Your program then prompts the user to enter an elapsed time, sets its elapsed
time in the Time object, and displays its hour, minute, and second.

(Hint: The initializer will extract the hour, minute, and second from the elapsed
time. The current elapsed time can be obtained using time.time(), as shown in
Listing 2.7, ShowCurrentTime.py.)'''

import time


class Time:
    # Construct a Time object
    def __init__(self):
        self.setTime(int(time.time()))

    # The accessor functions
    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    # The mutator function
    def setTime(self, elapsedTime):
        # Get the current second
        self.__second = elapsedTime % 60

        # Obtain the total minutes
        totalMinutes = elapsedTime // 60

        # Compute the current minute in the hour
        self.__minute = totalMinutes % 60

        # Obtain the total hours
        totalHours = totalMinutes // 60

        # Compute the current hour
        self.__hour = totalHours % 24


def main():
    # Create a Time object
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(
        currentTime.getSecond()))

    elapseTime = int(input("PLease enter the elapse time: "))
    currentTime.setTime(elapseTime)
    print("The hour:minute:second for elapse time is " + str(currentTime.getHour()) + ":" + str(
        currentTime.getMinute()) + ":" + str(currentTime.getSecond()))


main()  # Call the main function
