# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Modify weight in the nine tails problem) In the text, we assign the number of
the flips as the weight for each move. Assuming that the weight is three times
of the number of flips, revise the program.'''

from WeightedGraph import WeightedGraph
from WeightedGraph import WeightedEdge
from NineTailModel import NineTailModel
from NineTailModel import NUMBER_OF_NODES
from NineTailModel import getIndex
from NineTailModel import getNode
from NineTailModel import printNode
from NineTailModel import getFlippedNode

class WeightedNineTailModel(NineTailModel):
    # Construct a model
    def __init__(self):
        NineTailModel.__init__(self)  # Invoke superclass constructor

        # Create a graph
        vertices = [x for x in range(NUMBER_OF_NODES)]
        graph = WeightedGraph(vertices, getWeightedEdges())

        # Obtain a BSF tree rooted at the target node
        self.tree = graph.getShortestPath(511)

    def getNumberOfFlipsFrom(self, u):
        return self.tree.getCost(u) * 3  # Multiply the number of flips by 3 to get the weight


# Create all edges for the graph
def getWeightedEdges():
    # Store edges
    edges = []

    for u in range(NUMBER_OF_NODES):
        for k in range(9):
            node = getNode(u)  # Get the node for vertex u
            if node[k] == 'H':
                v = getFlippedNode(node, k)
                numberOfFlips = getNumberOfFlips(u, v)

                # Add edge (v, u) for a legal move from node u to node v
                edges.append(WeightedEdge(v, u, numberOfFlips))

    return edges


def getNumberOfFlips(u, v):
    node1 = getNode(u)
    node2 = getNode(v)

    count = 0  # Count the number of different cells
    for i in range(len(node1)):
        if node1[i] != node2[i]:
            count += 1

    return count


def main():
    # Prompt the user to enter nine coins H's and T's
    initialNode = input("Please enter an initial nine coin H's and T's: ").strip()

    # Create the WeightedNineTailModel
    model = WeightedNineTailModel()
    path = model.getShortestPath(getIndex(initialNode))

    print("The steps to flip the coins are ")
    for i in range(len(path)):
        printNode(getNode(path[i]))

    print("The number of flips is " +
          str(model.getNumberOfFlipsFrom(getIndex(initialNode))))


main()
