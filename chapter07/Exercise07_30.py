# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Culture: Chinese Zodiac) Simplify Listing 3.4 ChineseZodiac.py, using a list of
strings to store the animals' names.'''

year = int(input("Please enter a year: "))

months = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
          "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]

print(months[year % 12])
