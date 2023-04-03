# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Conversions between Celsius and Fahrenheit) Write a module that contains the
following two functions:

# Convert from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
# Convert from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit)

The formulas for the conversion are:

celsius = (5 / 9) * (fahrenheit - 32)
fahrenheit = (9 / 5) * celsius + 32

Write a test program that invokes these functions to display the following tables:'''


# Convert from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32


# Convert from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def main():
    # Print header of tables
    print("Celsius      Fahrenheit  |   Fahrenheit      Celsius")
    print("----------------------------------------------------")
    j = 120
    for i in range(40, 30, -1):
        # Display result
        print(f"%-1d%18.2f%6s%6d%18.2f" % (i, celsiusToFahrenheit(i), "|", (j), fahrenheitToCelsius(j)))
        j -= 10


main()
