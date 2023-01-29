#(Print a table) Write a program that displays the followng table:


#Display a table
print("a    a^2    a^3")
print("1    1       1")
print("2    4       8")
print("3    9       27")
print("4    16      64")

print("------------------------------")
print("Table with loop, Exercise01_04")
print("a \t\t a^2\t a")
for i in range(1, 5):
    print("{}\t\t {}\t\t {}".format(i, i ** 2, i ** 3))



