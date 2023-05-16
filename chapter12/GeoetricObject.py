class GeometricObject:
    def __init__(self, color="red", filled=True):
        self.__color = color  # Set color
        self.__filled = filled

    def getColor(self):
        return self.__color  # Get color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        if filled == 1:
            self.__filled = True

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)
