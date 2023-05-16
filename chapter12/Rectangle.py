from chapter12.GeoetricObject import GeometricObject


class Rectangle(GeometricObject):  # Rectangle is a subclass of GeometricObject
    def __init__(self, width=1, height=1):
        super().__init__()  # Invoke superclass's init method
        self.__width = width  # Set width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = self.__height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return "Rectangle: width = " + str(self.__width) + " height = " + str(self.__height)
