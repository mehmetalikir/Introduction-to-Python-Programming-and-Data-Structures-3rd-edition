# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Use the Rational class) Write a program that computes the following summation
series using the Rational class:'''

from Rational import Rational

sum = Rational(0, 1)

for i in range(1, 10):
    sum = sum + Rational(i, i + 1)

# Display results
print("Sum is " + str(sum))


