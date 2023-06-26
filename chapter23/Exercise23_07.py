# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Weighted 4 x 4 16 tails) Revise Listing 23.10, WeightedNineTail.py, for the
weighted 4 x 4 16 tails problem. Your program should read the model object
created from the preceding exercise.'''

from WeightedNineTailModel import WeightedNineTailModel
from NineTailModel import getIndex
from NineTailModel import getNode
from NineTailModel import printNode

def main():
    # Prompt the user to enter sixteen coins H's and T's
    initialNode = input("Please enter an initial sixteen coin H's and T's: ").strip()

    # Create the WeightedNineTailModel
    model = WeightedNineTailModel()

    # Get the shortest path from the initial node
    path = model.getShortestPath(getIndex(initialNode))

    print("The steps to flip the coins are:")
    for i in range(len(path)):
        printNode(getNode(path[i]))

    print("The number of flips is: " + str(model.getNumberOfFlipsFrom(getIndex(initialNode))))

main()
