#Exercise01_11
''' (Population projection) The US Census Bureau projects population based on the
following assumptions:
  - One birth every 7 seconds
  -	One death every 13 seconds
  - One new immigrant every 45 seconds

     Write a program to display the population for each of the next five years. Assume
that the current populations 312032486 and one year has 365 days. '''

a = 312032486
b = 60 * 24 * 365 *(60 / (13 - 7) ) + (60 / 45)

print("1st. Year Total Population: {:,}".format(a + b))
print("2nd. Year Total Population: {:,}".format(a + b * 2))
print("3rd. Year Total Population: {:,}".format(a + b * 3))
print("4th. Year Total Population: {:,}".format(a + b * 4))
print("5th. Year Total Population: {:,}".format(a + b * 5))

