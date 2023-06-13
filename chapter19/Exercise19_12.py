# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Parent reference for BST) Redefine TreeNode by adding a reference to a node's
parent, as shown below:

Reimplement the insert and delete methods in the BST class to update te
parent for each node in the tree. Add the following new method in BST:

    # Return the node for the specified element.
    # Return null if the element is not in the tree.
    def TreeNode getNode(self, element):

    # Return True if the node for the element is a leaf
    def isLeaf(self, element):

    # Return the path of elements from the specified element
    # to the root in a list.
    def getPath(self, e)

Write a test program that prompts the user to enter 10 integers, adds them to the
tree, deletes the first integer from the tree, and displays the paths for each leaf
node to the root.'''


def main():
    tree = BST()

    # Prompt the user to enter 10 integers
    numbers = input("Please enter 10 integers separated by spaces: ").split()
    for number in numbers:
        tree.insert(int(number))

    # Delete the first integer from the tree
    if len(numbers) > 0:
        firstNumber = int(numbers[0])
        tree.delete(firstNumber)

    # Display the paths for each leaf node to the root
    leafNodes = [node for node in tree.inorderList() if tree.isLeaf(node)]
    for leaf in leafNodes:
        path = tree.getPath(leaf)
        path.reverse()
        print("Path for leaf", leaf, "to root:", path)


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, e):
        return self.searchHelper(self.root, e)

    def searchHelper(self, current, e):
        if current is None:
            return None
        elif e < current.element:
            return self.searchHelper(current.left, e)
        elif e > current.element:
            return self.searchHelper(current.right, e)
        else:
            return current

    def insert(self, e):
        if self.root is None:
            self.root = self.createNewNode(e)
        else:
            parent = None
            current = self.root
            while current is not None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False

            if e < parent.element:
                parent.left = self.createNewNode(e)
                parent.left.parent = parent
            else:
                parent.right = self.createNewNode(e)
                parent.right.parent = parent

        self.size += 1
        return True

    def delete(self, e):
        node = self.getNode(e)
        if node is None:
            return False

        parent = node.parent

        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            successor = self.minimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

        self.size -= 1
        return True

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def createNewNode(self, e):
        return TreeNode(e)

    def getSize(self):
        return self.size

    def getNode(self, element):
        return self.searchHelper(self.root, element)

    def isLeaf(self, element):
        node = self.getNode(element)
        return node is not None and node.left is None and node.right is None

    def getPath(self, e):
        node = self.getNode(e)
        if node is None:
            return []

        path = []
        while node is not None:
            path.append(node.element)
            node = node.parent

        return path

    def inorderList(self):
        elements = []
        self.inorderListHelper(self.root, elements)
        return elements

    def inorderListHelper(self, node, elements):
        if node is not None:
            self.inorderListHelper(node.left, elements)
            elements.append(node.element)
            self.inorderListHelper(node.right, elements)



main()
