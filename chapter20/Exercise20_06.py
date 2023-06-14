# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Calculate minimum number of nodes for AVL Tree) Create a recursive method
which calculates the minimum nuber of noes required to create an AVL Tree
of a given height. For height 0, it can only have a single node. For height 1, the
minimum is two modes. For any height above (meaning that the root has a left
and right subtree) the formula to calculate the number of nodes is n(height) =
1 + n(height -1) + n(height-2), where n is the recursive function.
    Write s test program that prompts the user to enter the height, calls the function,
and prints the result'''


class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLTreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self._getBalance(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotateRight(node)
            else:
                node.left = self._rotateLeft(node.left)
                return self._rotateRight(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotateLeft(node)
            else:
                node.right = self._rotateRight(node.right)
                return self._rotateLeft(node)

        return node

    def _rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def _getBalance(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)


def calculateMinimumNodes(height):
    if height == 0:
        return 1
    elif height == 1:
        return 2
    else:
        return 1 + calculateMinimumNodes(height - 1) + calculateMinimumNodes(height - 2)


def main():
    height = int(input("Please enter the height: ")) # Tree of height 25 is: 317810.
    result = calculateMinimumNodes(height)

    avl_tree = AVLTree()
    for i in range(1, result + 1):
        avl_tree.insert(i)

    print(f"The minimum number of nodes required to create an AVL Tree of height {height} is: {result}.")


main()

"""[Feature] Calculate minimum number of nodes for AVL Tree

Implemented the recursive method to calculate the minimum number of nodes required to create an AVL Tree of a given height. The formula used is n(height) = 1 + n(height-1) + n(height-2), where n is the recursive function.

Added a test program to prompt the user for the height, call the function, and print the result.

Commit Details:
- Time Complexity: O(2^n)
- Space Complexity: O(n)

:sparkles: Added feature to calculate minimum nodes for AVL Tree
:chart_with_upwards_trend: Improved time complexity through recursive approach
:recycle: Refactored code for better readability"""
