# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compare the performance of different __hash__ implementations) Modify the
program implemented for Programing Exercise 21.2 and measure the time it
takes to create the 1000-Person objects and them to a set.
    Then change the __hash__ method implementation to the following (one at
a time, leaving the previous version in comments):
    * The number of characters in the first name, multiplied by the nuber of characters
    in the surname, multiplied by the integer representing the date of birth.
    * The sum of the integer representation of all characters in the first name and
    the surname
    * The number of characters in the first name, multiplied by the number of
    characters in the surname
    * The number of characters in the fist name
Your program should be similar to the one you made in Programing Exercise 21.2,
but do not print the Person objects(to avoid timing this action). Run the program
separately, changing the __hash__ implementation  each time to compare how
each implementation of the __hash__ method above impacts performance. '''

from datetime import datetime, timedelta


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

    # Implementation 1: The number of characters in the first name, multiplied by the number of characters
    # in the surname, multiplied by the integer representing the date of birth.
    def __hash__(self):
        return len(self.firstName) * len(self.surname) * int(self.dateOfBirth.strftime("%Y%m%d"))

    # Implementation 2: The sum of the integer representation of all characters in the first name and the surname
    def __hash__(self):
        return sum(ord(ch) for ch in self.firstName + self.surname)

    # Implementation 3: The number of characters in the first name, multiplied by the number of characters in the surname
    def __hash__(self):
        return len(self.firstName) * len(self.surname)

    # Implementation 4: The number of characters in the first name
    def __hash__(self):
        return len(self.firstName)

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

    print(f"Number of people: {len(people)}")
    for person in people:
        print(person)


main()
