# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Overriding __eq__ and __hash__) Create a Person class which contains a first
name, a surname, and a date of birth. Override the __eq__ method, so that two
Person objects are deemed to be equal if their name, surname and date of birth
are the same. Override the __hash__ , such that the hash code for
a Person object is their dae of birth represented as an integer(e.g 1970-01-15
would be 19700115). Use the datetime module to handle these dates and
conversion.
        Write a test program that uses a list of 10 first names, a list of 10 surnames
    and a start date of 1970-01-01, which is incremented a day at a time to generate
    1000 combinations of Person objects and adds them to a set. Print each name as
    you create it.
        Print each name as you see create it. To see how the __eq__ and __hash__
        methods are used this progarm, add a print statement(e.g, print("hash")) to
        each of these, so you can see when they are executed.'''

from datetime import datetime
from datetime import timedelta

class Person:
    # The constructor sets the names and DOB
    def __init__(self, firstName, surname, dateOfBirth):
        self.firstName = firstName
        self.surname = surname
        self.dateOfBirth = dateOfBirth

    # Checks for equality based on names and DOB
    def __eq__(self, other):

        return self.firstName == other.firstName \
               and self.surname == other.surname \
               and self.dateOfBirth == other.dateOfBirth

    # The hash is obtained by converting the DOB to an integer
    def __hash__(self):
        return int(self.dateOfBirth.strftime("%Y%m%d"))

    def __str__(self):
        return f'{self.firstName} {self.surname} {self.dateOfBirth}'

def main():
    firstNames = ['Aaron', 'Brigit', 'Peter', 'Richard', 'Paul', 'Sophie', 'Liz', 'Louis', 'Georgina', 'Sasha']
    surNames = ['Smith', 'Jones', 'Peters', 'Wolf', 'Martin', 'Baker', 'Miller', 'Gibson', 'Osbourne', 'Fann']

    startDate = datetime.strptime("1970-01-01", "%Y-%m-%d")
    people = set()

    # Generates Person objects by combining the first names and surnames
    count = 0
    for firstName in firstNames:
        for surname in surNames:
            # For each name combination, it generates multiple people with different DOBs
            for i in range(10):
                p = Person(firstName, surname, startDate + timedelta(days=count))
                count += 1
                people.add(p)
                print(p)
                print(p.__hash__())



main()


