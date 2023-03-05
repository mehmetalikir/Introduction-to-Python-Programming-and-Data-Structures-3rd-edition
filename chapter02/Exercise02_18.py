# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

import time

#Exercise02_18
''' (Current time) Listing 2.7, ShowCurrrentTime.py, gives a program that display 
the current time in GMT. Revise the program so that it prompts the user to enter 
the time zone in hours away from (offset to) GMT and displays the time int the 
specified time zone.'''

"Enter the time one offset to GMT: -5"
"Current time is 5 : 0 : 19"

currentTime = time.time() # Get current time

# Obtain the total sconds since midnight, Jan 1, 1970
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
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour,
      ":", currentMinute, ":", currentSecond, "GMT")
