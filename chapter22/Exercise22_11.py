# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Variation of the nine tail problem) In the nine tail problem, when you flip a
head, the horizontal and vertical neighboring cells are also flipped. Rewrite the
program, assuming that all neighboring cells including the diagonal neighbors
are also flipped.'''

from Queue import Queue
def main():
    # Prompt the user to enter nine coins H's and T's
    initialNode = \
        input("Please enter an initial nine coin H's and T's: ").strip()

    # Create the NineTaileModel
    model = NineTailModel()
    path = model.getShortestPath(getIndex(initialNode))

    print("The steps to flip the coins are ")
    for i in range(len(path)):
        printNode(getNode(path[i]))


from Graph import Graph

NUMBER_OF_NODES = 512


class NineTailModel:
    def __init__(self):
        edges = getEdges()

        # Create a graph
        vertices = [x for x in range(NUMBER_OF_NODES)]
        graph = Graph(vertices, edges)

        # Obtain a BSF tree rooted at the target node
        self.tree = graph.bfs(511)

    def getShortestPath(self, nodeIndex):
        return self.tree.getPath(nodeIndex)


def printNode(node):
    for i in range(9):
        if i % 3 != 2:
            print(node[i], end=" ")
        else:
            print(node[i])

    print()


# Create all edges for the graph
def getEdges():
    edges = []  # Store edges
    for u in range(NUMBER_OF_NODES):
        for k in range(9):
            node = getNode(u)  # Get the node for vertex u
            if node[k] == 'H':
                v = getFlippedNode(node, k)
                # Add edge (v, u) for a legal move from node u to node v
                edges.append([v, u])

    return edges


def getFlippedNode(node, position):
    row = position // 3
    column = position % 3

    flipACell(node, row, column)
    flipACell(node, row - 1, column)
    flipACell(node, row + 1, column)
    flipACell(node, row, column - 1)
    flipACell(node, row, column + 1)

    return getIndex(node)


def getIndex(node):
    result = 0

    for i in range(9):
        if node[i] == 'T':
            result = result * 2 + 1
        else:
            result = result * 2 + 0

    return result


def flipACell(node, row, column):
    if row >= 0 and row <= 2 and column >= 0 and column <= 2:
        # Within the boundary
        if node[row * 3 + column] == 'H':
            node[row * 3 + column] = 'T'  # Flip from H to T
        else:
            node[row * 3 + column] = 'H'  # Flip from T to H


def getNode(index):
    result = 9 * [' ']

    for i in range(9):
        digit = index % 2
        if digit == 0:
            result[8 - i] = 'H'
        else:
            result[8 - i] = 'T'
        index = index // 2

    return result


def getFlippedNode(node, position):
    row = position // 3 #.145
    column = position % 3 #.145

    flipACell(node, row, column)
    flipACell(node, row - 1, column)
    flipACell(node, row + 1, column)
    flipACell(node, row, column - 1)
    flipACell(node, row, column + 1)
    flipACell(node, row - 1, column - 1)  # Flip diagonal neighbors
    flipACell(node, row - 1, column + 1)  # Flip diagonal neighbors
    flipACell(node, row + 1, column - 1)  # Flip diagonal neighbors
    flipACell(node, row + 1, column + 1)  # Flip diagonal neighbors

    return getIndex(node)


main()

'''Please enter an initial nine coin H's and T's: H H H H H H H h h
The steps to flip the coins are 
H H H
H H H
H H H

T T T
T T T
T T T'''
