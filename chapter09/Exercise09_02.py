# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The Petroleum class) Design a class named Petroleum to represent a country’s Petroleum
products that contains:

    ■ A private string data field named name for the petroleum product’s name.
    ■ A private string data field named grade for the petroleum product’s octane
    grade.
    ■ A private float data field named lastMonthPrice that stores the last month price of
    the product.
    ■ A private float data field named currentPrice that stores the current price of
    the product.
    ■ A constructor that creates a petroleum's product with the specified name, grade
    last price, and current price.
    ■ A get method for returning petroleum product’s name.
    ■ A get method for returning the petroleum product’s grade
    ■ Get and set methods for getting/setting the stock’s last month price.
    ■ Get and set methods for getting/setting the stock’s current price.
    ■ A method named getChangePercent() that returns the percentage changed
    from previousClosingPrice to currentPrice.

Draw the UML diagram for the class, and then implement the class. Write a test
program that creates a Petroleum object with the product name Gasoline, the
grade Regular, the last month price of 3.5, and the current price of 3.32, and
display the price-change percentage'''


class Petroleum:
    # Construct a Petroleum object
    def __init__(self, name, grade, lastMonthPrice, currentPrice):
        self.__grade = grade
        self.__name = name
        self.__currentPrice = currentPrice
        self.__lastMonthPrice = lastMonthPrice

    def getName(self):
        return self.__name

    def getGrade(self):
        return self.__grade

    def getLastPrice(self):
        return self.__lastMonthPrice

    def setLastPrice(self):
        return self.__lastMonthPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self):
        return self.__currentPrice

    def getChangePercent(self):
        previousClosingPrice = self.getLastPrice()
        currentPrice = self.getCurrentPrice()

        return format((currentPrice - previousClosingPrice)
                      * 100 / self.getLastPrice(), "5.2f")


def main():
    # Create a Petroleum's product
    product = Petroleum("Gasoline", "Regular", 3.5, 3.32)
    print(f"The price change is {product.getChangePercent()}%")


main()
