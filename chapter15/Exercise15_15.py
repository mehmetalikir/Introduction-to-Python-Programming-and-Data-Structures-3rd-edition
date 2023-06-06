# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Calculate number of offspring) Given the following definition of a Person class:

    And following statement create a family tree:

    Write a recursive function that calculates the number of offspring for a given
    person in the family tree. For instance, Helen has 6 offspring'''


class Person:
    def __init__(self, name, children):
        self.name = name
        self.children = children


# Calculate the number of offspring for a given person in the family tree
def calculateOffspring(person):
    if person.children is None: # Base case
        return 0
    offspringCount = 0
    for child in person.children:
        offspringCount += 1 + calculateOffspring(child) # Recursive call
    return offspringCount


def main():
    p1 = Person("Eric", None)
    p2 = Person("Ariana", None)
    p3 = Person("Mark", [p1, p2])
    p4 = Person("John", None)
    p5 = Person("Mary", [p3, p4])
    p6 = Person("Edward", None)
    p7 = Person("Helen", [p5, p6])

    offspringCount1 = calculateOffspring(p7)
    offspringCount2 = calculateOffspring(p3)

    # Display result
    print(f"{p7.name} has {offspringCount1} children")
    print(f"{p3.name} has {offspringCount2} children")


main()
