# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

#Exercise02_05
''' (Financial application: calculate tips) Write a program that reads the subtotal
and the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, th program displays 1.5
as the gratuity and 11.5 as the total.'''

#Enter the subtotal
subtotal = float(input('Enter the subtotal : '))

#Enter the gratuity rate
rate = float(input('Enter the gratuity rate : '))

#Display result
result = subtotal * (rate / 100)
print('The gratuity is ', "%.2f" % result, ' and total is ', "%.2f" % (subtotal + result))