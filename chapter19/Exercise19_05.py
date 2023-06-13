# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement postorder without using recursion) Implement the postorder
method in BST using a stack instead of recursion'''

from collections import deque


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1  # Increase tree size
        return True  # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    def postorderIterative(self):
        if self.root is None:
            return

        stack = deque()
        output = deque()
        stack.append(self.root)

        while stack:
            current = stack.pop()
            output.appendleft(current.element)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        for element in output:
            print(element, end=' ')
        print()


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None


def main():
    tree = BST()
    inputFile = open("JackAndJill.txt", "r")

    fileContent = inputFile.read()
    inputFile.close()
    words = fileContent.split()
    for word in words:
        tree.insert(word.lower())

    tree.postorderIterative()


main()
