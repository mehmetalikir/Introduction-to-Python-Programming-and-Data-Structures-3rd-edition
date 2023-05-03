# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Car class) Design a class named Car to represent a car. The class contains:

    ■ Three constants named SEDAN, COUPE, and HATCHBACK with the values 1, 2,
    and 3 to denote the body type.
    ■ A private int data field named bodyType that specifies the body type of the car.
    ■ A private bool data field named forSale that specifies whether the car is sale (the
    default is False).
    ■ A private float data field named ccPower that specifies the engine power of the car.
    ■ A private string data field named color that specifies the color of the car.
    ■ The accessor and mutator methods for all four data fields.
    ■ A constructor that creates a car with the specified body type (default SEDAN), engine
    power (default 1000), color (default white), and for sale (default False).

Draw the UML diagram for the class and then implement the class. Write a test
program that creates two Car objects. The first object is COUPE, 1800cc engine
power, color white, and is not for sale. The second object is a SEDAN, 2400cc engine
power, color red, and is not for sale. Display each car’s number of doors, color
engine power, and for sale status.'''

# Global constants to hold number of doors as per body type
SEDAN = 4
COUPE = 2
HATCHBACK = 4
HATCHBACKCOUPE = 2


# Design a class named Car
class Car:

    def __init__(self, bodyType, ccPower, color, forSale):
        self.__bodyType = bodyType
        self.__ccPower = ccPower
        self.__color = color
        self.__forSale = forSale

    def getBodyType(self):
        return self.__bodyType

    def getCcPower(self):
        return self.__ccPower

    def getColor(self):
        return self.__color

    def isForSale(self):
        return self.__forSale


# Display properties
def displayProperties(c):
    print("Number of doors:", c.getBodyType(), "\nColor:", c.getColor(), "\nEngine power:", c.getCcPower(),
          "\nCar is for sale\n" if c.isForSale() else "\nCar is not for sale\n")


def main():
    # Create a Car object
    car1 = Car(COUPE, 1800, "white", True)
    displayProperties(car1)

    # Create a Car object
    car2 = Car(SEDAN, 2400, "red", False)
    displayProperties(car2)


main()  # Call the main function
