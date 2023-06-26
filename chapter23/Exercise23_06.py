# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Weighted 4 x 4 16 tails model) The weighted nine tails problem in the text
uses a 3 x 3 matrix. Assume that you have 16 coins placed in a 4 x 4 matrix.
Create a new model class named WeightedTailModel16. Create an instance
of the model and save the object into a file named WeightedTailModel16.dat.'''



from WeightedGraph import WeightedEdge
from WeightedGraph import WeightedGraph


import pickle


class WeightedTailModel16:
    def __init__(self):
        self.NUMBER_OF_NODES = 2 ** 16
        self.tree = None
        self.buildModel()

    def buildModel(self):
        vertices = [x for x in range(self.NUMBER_OF_NODES)]
        edges = self.getWeightedEdges()
        graph = WeightedGraph(vertices, edges)
        self.tree = graph.getShortestPath(self.NUMBER_OF_NODES - 1)  # Target node index

    def getWeightedEdges(self):
        edges = []

        for u in range(self.NUMBER_OF_NODES):
            node = self.getNode(u)
            for k in range(16):
                row = k // 4
                col = k % 4
                if node[row][col] == 'H':
                    v = self.getFlippedNode(node, k)
                    numberOfFlips = self.getNumberOfFlips(u, v)
                    edges.append(WeightedEdge(v, u, numberOfFlips))

        return edges

    def getNode(self, index):
        node = [['H'] * 4 for _ in range(4)]
        for i in range(16):
            row = i // 4
            col = i % 4
            if (index >> i) % 2 == 0:
                node[row][col] = 'T'
        return node

    def getFlippedNode(self, node, position):
        row = position // 4
        col = position % 4
        flippedNode = [list(row) for row in node]  # Create a copy of the node
        flippedNode[row][col] = 'H' if node[row][col] == 'T' else 'T'
        if row > 0:
            flippedNode[row - 1][col] = 'H' if node[row - 1][col] == 'T' else 'T'
        if row < 3:
            flippedNode[row + 1][col] = 'H' if node[row + 1][col] == 'T' else 'T'
        if col > 0:
            flippedNode[row][col - 1] = 'H' if node[row][col - 1] == 'T' else 'T'
        if col < 3:
            flippedNode[row][col + 1] = 'H' if node[row][col + 1] == 'T' else 'T'
        return flippedNode

    def getNumberOfFlips(self, u, v):
        count = 0
        for i in range(4):
            for j in range(4):
                if u[i][j] != v[i][j]:
                    count += 1
        return count


# Create an instance of the WeightedTailModel16
model = WeightedTailModel16()

# Save the object to a file
filename = "WeightedTailModel16.dat"
with open(filename, "wb") as file:
    pickle.dump(model, file)

print("WeightedTailModel16 object saved to", filename)
