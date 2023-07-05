# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find u with smallest cost[u] efficiently) The getShortestPath method
finds a u with the smallest cost[u] using a linear search, which takes O(|V|).
The search time can be reduced to O(log |V|) using an AVL tree. Modify the
method using an AVL tree to store the vertices in V – T. Use Listing 23.8,
TestShortestPath.py, to test your new implementation.'''

from WeightedGraph import WeightedGraph

INFINITY = float('inf')  # Infinity value

# Test program
graph1 = WeightedGraph(vertices=["A", "B", "C", "D", "E", "F"],
                       edges=[
                           (0, 1, 2), (0, 3, 8),
                           (1, 0, 2), (1, 2, 7), (1, 3, 3),
                           (2, 1, 7), (2, 3, 4), (2, 4, 5), (2, 5, 6),
                           (3, 0, 8), (3, 1, 3), (3, 2, 4), (3, 4, 6),
                           (4, 2, 5), (4, 3, 6), (4, 5, 9),
                           (5, 2, 6), (5, 4, 9),
                       ])
graph1.addVertex("Chicago")
graph1.addVertex("Seattle")
graph1.addVertex("San Francisco")
graph1.addVertex("Denver")
graph1.addVertex("Kansas City")

chicagoIndex = graph1.getIndex("Chicago")
chicagoIndex = graph1.getIndex("Seattle")
chicagoIndex = graph1.getIndex("San Francisco")
chicagoIndex = graph1.getIndex("Denver")
chicagoIndex = graph1.getIndex("Kansas City")

tree2 = graph1.getShortestPath(chicagoIndex)
tree2.printAllPaths()
