# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Working with tuples) Write a program that uses a loop to create a tuple containing
the numbers from 0 to 999_999. Add another loop that does the same with a list.
Finally, add two loops that iterate over the tuple and the list and sum up all
the integers contained in each list. Measure and print the time it takes to create
the tuple/list and then to do the processing. Note: To measure the time in seconds
you can take a timestamp before you start execution(time.time()) take a timestamp
after execution and subtract the first from the second'''

import time

startTime = time.time()  # Get start time
# Create a tuple containing the numbers from 0 to 999_999
t1 = tuple(i for i in range(999_999_9))
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print("Tuple creation time: ", runTime, "milliseconds")


startTime = time.time()  # Get start time
t2 = tuple([x for x in range(0, 999_999_9)])
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print("List creation time: ", runTime, "milliseconds")


startTime = time.time()  # Get start time
sumList = 0
for item in t1:
    sumList += item
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print("Tuple processing time: ", runTime, "milliseconds")


startTime = time.time()  # Get start time
sumList = 0
for item in t2:
    sumList += item
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print("List processing time: ", runTime, "milliseconds")