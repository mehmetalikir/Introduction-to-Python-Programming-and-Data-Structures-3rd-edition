import math


class Complex:
    def __init__(self, a=0.0, b=0.0):
        self.a = a
        self.b = b

    # Add a complex number to this rational number
    def __add__(self, secondComplex):
        return Complex(self.a + secondComplex.a,
                       self.b + secondComplex.b)

    # Subtract a complex number from this complex number
    def __sub__(self, secondComplex):
        return Complex(self.a - secondComplex.a,
                       self.b - secondComplex.b)

    # Multiply a complex number to this complex
    def __mul__(self, secondComplex):
        return Complex(self.a * secondComplex.a - self.b * secondComplex.b,
                       self.b * secondComplex.a + self.a * secondComplex.b)

    # Divide a complex number by this complex number
    def __truediv__(self, secondComplex):
        return Complex((self.a * secondComplex.a + self.b * secondComplex.b) /
                       (math.pow(secondComplex.a, 2) + math.pow(secondComplex.b, 2)),
                       (self.b * secondComplex.a - self.a * secondComplex.b) /
                       (math.pow(secondComplex.a, 2) + math.pow(secondComplex.b, 2)))

    # Absolute value for a complex number
    def __abs__(self):
        return math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))

    # Return a string representation
    def __str__(self):
        if self.b == 0:
            return self.a
        else:
            return format(f"({self.a} + {self.b}i)")

    # Return real part of complex number
    def getRealPart(self):
        return self.a

    # Return imaginary part of complex number
    def getImaginaryPart(self):
        return self.b
