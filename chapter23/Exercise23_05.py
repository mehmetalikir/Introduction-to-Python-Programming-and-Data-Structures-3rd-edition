# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Prove or disprove) The conjecture is that both NineTailModel and
WeightedNineTailModel result in the same shortest path. Write a program to
prove or disprove it. (Hint: Let tree1 and tree2 denote the trees rooted at node
511 obtained from NineTailModel and WeightedNineTailModel, respectively.
If the depth of a node u is the same in tree1 and in tree2, the length of
the path from u to the target is the same.)'''

from NineTailModel import NineTailModel
from WeightedNineTailModel import WeightedNineTailModel
from NineTailModel import NUMBER_OF_NODES


def compareShortestPaths():
    # Create the NineTailModel
    model1 = NineTailModel()
    tree1 = model1.tree

    # Create the WeightedNineTailModel
    model2 = WeightedNineTailModel()
    tree2 = model2.tree

    # Compare the depth of each node in the trees
    for nodeIndex in range(NUMBER_OF_NODES):
        path1 = tree1.getPath(nodeIndex)
        path2 = tree2.getPath(nodeIndex)

        depth1 = len(path1) - 1
        depth2 = len(path2) - 1

        if depth1 != depth2:
            return False

        print("Node:", nodeIndex)
        print("Path in NineTailModel:", path1)
        print("Path in WeightedNineTailModel:", path2)
        print()

    return True


result = compareShortestPaths()

if result:
    print("The shortest paths are the same.")
else:
    print("The shortest paths are different.")
