# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Current time) Revise Programming Exercise 2.18 to display the hour using a
12-hour clock.'''

import time

offset = int(input("Please enter the time one offset to GMT: "))

currentTime = time.time()  # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = (totalHours + offset) % 24
str = ""
if currentHour < 12:
    str = "AM"
else:
    str = "PM"
currentHour = currentHour % 12

# Display result
print("Current time is {:02d}".format(currentHour),
      ":", currentMinute, ":", currentSecond, str)
