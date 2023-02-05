#Exercise01_10
''' (Average speed in kilometers)  Assume a runner runs 2.5 miles in 23 minutes and
45 seconds. Write a program that displays the average speed in kilometers per
hour.(Note that 1 mile is 1.6 kilometers.)'''
#Speed = Distance ÷ Time

#Convert mile to kilometer
distance = 2.5 * 1.6
print('Distance:', distance, ''''Km''')

# Convert minute to second
time = 23 * 60 + 45
print('Time :', time, ''''Seconds''')

# If runner runs 4 km in 1425 seconds then runner runs x km in hour
print('Average speed in kilometers: {:.2f}'.format(distance * 3600 / time))

