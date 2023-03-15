# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Business: check ISBN-10) An ISBN-10 (International Standard Book Number)
consists of 10 digits: d1d2d3d4d5d6d7d8d9d10. The last digit, d10, is a checksum,
which is calculated from the other nine digits using the following formula:
(d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 +
d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
If the checksum is 10, the last digit is denoted as X according to the ISBN-10
convention. Write a program that prompts the user to enter the first 9 digits and
displays the checksum. Your program should read the input as an integer if the
integer starts with 0s, don't enter these zeros in the input. '''

# Prompt the user to enter the first 9 digits of a 10-digit ISBN
isbn = int(input("Please enter the first 9 digits of an ISBN as integer: "))

# Compute the checksum
d1 = isbn // 100000000
digit = isbn % 100000000
d2 = digit // 10000000
digit %= 10000000
d3 = digit // 1000000
digit %= 1000000
d4 = digit // 100000
digit %= 100000
d5 = digit // 10000
digit %= 10000
d6 = digit // 1000
digit %= 1000
d7 = digit // 100
digit %= 100
d8 = digit // 10
digit %= 10
d9 = digit

str = ""
d10 = (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
if d10 == 10:
    str = "X"
else:
    str = d10

# Display result
print("The ISBN-10 number is ", d1,d2,d3,d4,d5,d6,d7,d8,d9,str)
