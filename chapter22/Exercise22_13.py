# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Induced subgraph) Given an undirected graph G = (V, E) and an integer
k, find an induced subgraph H of G of maximum size such that all vertices
of H have a degree 7 = k, or conclude that no such induced subgraph exists.
Implement the function with the following header:

    def maxInducedSubgraph(graph,k):

The method returns None if such a subgraph does not exist.
(Hint: An intuitive approach is to remove vertices whose degree is less than k.
As vertices are removed with their adjacent edges, the degrees of other vertices
may be reduced. Continue the process until no vertices can be removed, or all
the vertices are removed.)
'''

from Graph import Graph

NUMBER_OF_NODES = 2 ** 16


class TailModel16:
    def __init__(self):
        edges = self.getEdges()

        # Create a graph
        vertices = [x for x in range(NUMBER_OF_NODES)]
        graph = Graph(vertices, edges)

        # Obtain a BFS tree rooted at the target node
        self.tree = graph.bfs(NUMBER_OF_NODES - 1)

    def getShortestPath(self, nodeIndex):
        return self.tree.getPath(nodeIndex)

    @staticmethod
    def printNode(node):
        for i in range(16):
            if i % 4 != 3:
                print(node[i], end=" ")
            else:
                print(node[i])
        print()

    @staticmethod
    def getEdges():
        edges = []  # Store edges
        for u in range(NUMBER_OF_NODES):
            for k in range(16):
                node = TailModel16.getNode(u)  # Get the node for vertex u
                if node[k] == 'H':
                    v = TailModel16.getFlippedNode(node, k)
                    # Add edge (v, u) for a legal move from node u to node v
                    edges.append([v, u])
        return edges

    @staticmethod
    def getFlippedNode(node, position):
        row = position // 4
        column = position % 4

        TailModel16.flipACell(node, row, column)
        TailModel16.flipACell(node, row - 1, column)
        TailModel16.flipACell(node, row + 1, column)
        TailModel16.flipACell(node, row, column - 1)
        TailModel16.flipACell(node, row, column + 1)

        return TailModel16.getIndex(node)

    @staticmethod
    def getIndex(node):
        result = 0
        for i in range(16):
            if node[i] == 'T':
                result = result * 2 + 1
            else:
                result = result * 2 + 0
        return result

    @staticmethod
    def flipACell(node, row, column):
        if 0 <= row < 4 and 0 <= column < 4:
            if node[row * 4 + column] == 'H':
                node[row * 4 + column] = 'T'  # Flip from H to T
            else:
                node[row * 4 + column] = 'H'  # Flip from T to H

    @staticmethod
    def getNode(index):
        result = [' ' for _ in range(16)]
        for i in range(16):
            digit = index % 2
            if digit == 0:
                result[15 - i] = 'H'
            else:
                result[15 - i] = 'T'
            index = index // 2
        return result


def main():
    # Create the TailModel16
    model = TailModel16()

    # Save the model object to a file
    with open('Exercise22_12.dat', 'wb') as file:
        import pickle
        pickle.dump(model, file)
    print("Model object saved to Exercise22_12.dat")


def maxInducedSubgraph(graph, k):
    # Create a copy of the original graph
    subgraph = graph.copy()

    # Remove vertices with degree less than k iteratively
    while True:
        removed_vertices = []
        for vertex in subgraph.vertices():
            if subgraph.degree(vertex) < k:
                removed_vertices.append(vertex)

        if len(removed_vertices) == 0:
            break

        # Remove the vertices and their adjacent edges
        for vertex in removed_vertices:
            subgraph.remove_vertex(vertex)

    # Check if any vertices remain in the subgraph
    if subgraph.num_vertices() > 0:
        return subgraph
    else:
        return None


if __name__ == '__main__':
    main()
