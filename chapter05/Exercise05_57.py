# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Business: check ISBN-13) ISBN-13 is a new standard for identifying books. It
uses 13 digits d1d2d3d4d5d6d7d8d9d10d11d12d13. The last digit d13 is a checksum,
which is calculated from the other digits using the following formula:

    10 - (d1 + 3d2 + d3 + 3d4 + d5 + 3d6 + d7 + 3d8 + d9 + 3d10 + d11 + 3d12)%10

If the checksum is 10, replace it with 0. Your program should read the input as a
string.'''

# Prompt the user to enter the first 12 digits of an ISBN as string
isbn = input("Enter the first 12 digits of an ISBN as a string: ")

# Assign values
checksum, sum = 0, 0

# Calculate the checksum
for i in range(0, len(isbn) - 1):
    if i % 2 == 0:
       sum +=  int(isbn[i])
    else:
        sum += int(isbn[i] * 3)

# Calculate from the other digits using the following formula
checksum = 10 - (sum % 10)
if checksum == 10:
    checksum = 0

# Display result
print("The ISBN number is ",isbn,checksum)