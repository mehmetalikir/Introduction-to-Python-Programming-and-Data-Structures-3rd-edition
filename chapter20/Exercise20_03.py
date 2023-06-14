# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Parent reference for BST) Suppose that the TreeNode class defined in BST contains
a reference to the node’s parent, as shown in Programming Exercise 19.12.
Implement the AVLTree class to support this change. Write a test program that
adds numbers 1, 2, . . . , 100 to the tree and displays the paths for all leaf nodes.'''


class AVLTree:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root is None:
            self.root = AVLNode(value)
        else:
            self.root = self._InsertRecursive(value, self.root)

    def _InsertRecursive(self, value, node):
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._InsertRecursive(value, node.left)
        else:
            node.right = self._InsertRecursive(value, node.right)

        node.UpdateHeight()
        return self.Balance(node)

    def Balance(self, node):
        if node.GetBalanceFactor() > 1:
            if node.left.GetBalanceFactor() < 0:
                node.left = self.RotateLeft(node.left)
            return self.RotateRight(node)
        elif node.GetBalanceFactor() < -1:
            if node.right.GetBalanceFactor() > 0:
                node.right = self.RotateRight(node.right)
            return self.RotateLeft(node)
        return node

    def RotateLeft(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.UpdateHeight()
        newRoot.UpdateHeight()
        return newRoot

    def RotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.UpdateHeight()
        newRoot.UpdateHeight()
        return newRoot

    def DisplayLeafPaths(self):
        self._DisplayLeafPathsRecursive(self.root, [])

    def _DisplayLeafPathsRecursive(self, node, path):
        if node is None:
            return

        path.append(node.value)

        if node.left is None and node.right is None:
            print("Path:", path)

        self._DisplayLeafPathsRecursive(node.left, path)
        self._DisplayLeafPathsRecursive(node.right, path)

        path.pop()


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def UpdateHeight(self):
        self.height = 1 + max(self.GetLeftHeight(), self.GetRightHeight())

    def GetBalanceFactor(self):
        return self.GetLeftHeight() - self.GetRightHeight()

    def GetLeftHeight(self):
        return self.left.height if self.left else 0

    def GetRightHeight(self):
        return self.right.height if self.right else 0


def main():
    avlTree = AVLTree()

    for i in range(1, 101):
        avlTree.Insert(i)

    avlTree.DisplayLeafPaths()


main()
