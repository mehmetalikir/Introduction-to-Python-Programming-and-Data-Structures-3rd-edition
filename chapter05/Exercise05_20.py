# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:'''

for i in range(1, 7):
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print('')
print("-----------------")
for i in range(6, 0, -1):
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print('')
print("-----------------")
i = 1
while i <= 6:
    j = 6 - i
    while j >= 1:
        print(end=" ")
        j -= 1
    k = i
    while k >= 1:
        print(k, end="")
        k -= 1
    print('')
    i += 1
print("-----------------")
i = 1
while i <= 8:
    j = 1
    while j < i:
        print(end=" ")
        j += 1
    k = 1
    while k < 8 - i:
        print(k, end="")
        k += 1
    print('')
    i += 1



