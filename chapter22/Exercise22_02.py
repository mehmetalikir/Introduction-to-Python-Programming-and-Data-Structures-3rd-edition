# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Adjacency Matrix to Adjacency List) Write a method that converts an adjacency
matrix of a directed graph to an adjacency list. Create a test program that uses
the method to convert the following adjacency matrix to an adjacency list:
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]  # Train Users
The above adjacency matrix contains a list of tasks involved in a project to deploy
bew software.'''

from collections import defaultdict


def convertToAdjacencyList(adjacencyMatrix):
    adjacencyList = defaultdict(list)
    for i in range(len(adjacencyMatrix)):
        for j in range(len(adjacencyMatrix[i])):
            if adjacencyMatrix[i][j] == 1:
                adjacencyList[i].append(j)
    return adjacencyList


def main():
    adjMatrix = [
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]  # Train Users
    ]
    adjList = convertToAdjacencyList(adjMatrix)
    print("Adjacency Matrix:")
    print(adjMatrix)

    print("Adjacency List:")
    for i in adjList:
        print(i, end="")
        for j in adjList[i]:
            print(" -> {}".format(j), end="")
        print()


main()
