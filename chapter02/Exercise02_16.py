# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_16
#(Phisics: acceleration)
"""
Average acceleration is defined as the change of velocity
divided by the time taken to make the change, as shown in
the following formula:
a = (v1 - v0) / t
"""
#Enter the starting velocity in meters/second
v0 = float(input("Enter the starting velocity in meters/second" \
"for example 5.5:\t"))

#Enter the ending velocity in meters/second
v1 = float(input("Enter the ending velocity in meters/second" \
"for example 50.9:\t"))

#Enter the time span in seconds
t = float(input("Enter the time span in seconds"\
"for example 4.5:\t"))

a = (v1 - v0) / t

print("The average acceleration is:",a)
