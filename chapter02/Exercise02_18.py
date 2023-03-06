# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

import time

#Exercise02_18
''' (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that display 
the current time in GMT. Revise the program so that it prompts the user to enter 
the time zone in hours away from (offset to) GMT and displays the time int the 
specified time zone.'''

"example output  = Current time is 5 : 0 : 19"


offset = float(input("Enter the time one offset to GMT: -5\n"))

currentTime = time.time() # Get current time

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
currentHour = (int)(totalHours + offset) % 24

# Display results
print("Current time is {:02d}".format(currentHour),
      ":", currentMinute, ":", currentSecond, "GMT")
