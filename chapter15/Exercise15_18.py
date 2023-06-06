# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Towers of Hanoi) Modify Listing 15.8, TowersOfHanoi.py, so that the program
finds the number of moves needed to move n disks from tower A to tower B.
(Hint: Use a global variable and increment it for every move.)'''


# The function for finding the solution to move n disks from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global count

    if n == 1:  # Stopping condition
        #        print("Move disk " + str(n) + " from " +
        #            fromTower + " to " + toTower)
        count += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        #        print("Move disk " + str(n) + " from " +
        #            fromTower + " to " + toTower)
        count += 1
        moveDisks(n - 1, auxTower, toTower, fromTower)

# Assign value
count = 0

n = int(input("Please enter number of disks: "))

# Find the solution recursively
print("The moves are:")
moveDisks(n, 'A', 'B', 'C')

# Display result
print("Number of moves is " + str(count))

