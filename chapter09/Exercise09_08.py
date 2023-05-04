# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Stopwatch) Design a class named StopWatch. The class contains:

 ■ The private data fields startTime and endTime with get methods.
 ■ A constructor that initializes startTime with the current time.
 ■ A method named start() that resets the startTime to the current time.
 ■ A method named stop() that sets the endTime to the current time.
 ■ A method named getElapsedTime() that returns the elapsed time for the
   stopwatch in milliseconds.

Draw the UML diagram for the class and then implement the class. Write a test
program that measures the execution time of finding the number 99 from a loop
generating random numbers in range of 1 to 1_000_000'''

import time
import random


class StopWatch:
    # Construct a StopWatch object
    def __init__(self):
        self.start()

    # The accessor functions
    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))


def main():
    # Create a StopWatch object
    stopWatch = StopWatch()
    while True:
        number = random.randint(0, 1_000_000)
        if number == 99:
            break
    stopWatch.stop()

    print("The loop time to find first 99 is", stopWatch.getElapsedTime(), "milliseconds")


main()  # Call the main function
