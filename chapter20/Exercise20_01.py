# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display AVL tree graphically) Write Tkinter that displays an AVL tree
along with its balance factor for each node.'''

import tkinter as tk

class AvlTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balanceFactor = 0

class AvlTreeDisplay:
    def __init__(self, tree):
        self.tree = tree
        self.root = tree.root

        self.window = tk.Tk()
        self.window.title("AVL Tree Display")

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        self.drawTree(self.root, 400, 30, 300)

        self.window.mainloop()

    def drawTree(self, node, x, y, hGap):
        if node:
            # Draw the node
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.key))

            # Draw the balance factor
            self.canvas.create_text(x, y+30, text="BF: " + str(node.balanceFactor))

            # Draw left subtree
            if node.left:
                self.canvas.create_line(x, y+20, x-hGap, y+80)
                self.drawTree(node.left, x-hGap, y+80, hGap//2)

            # Draw right subtree
            if node.right:
                self.canvas.create_line(x, y+20, x+hGap, y+80)
                self.drawTree(node.right, x+hGap, y+80, hGap//2)

class AvlTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AvlTreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.balanceFactor = self.getHeight(node.right) - self.getHeight(node.left)

        return self.balance(node)

    def balance(self, node):
        if node.balanceFactor > 1:
            if node.right.balanceFactor < 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        elif node.balanceFactor < -1:
            if node.left.balanceFactor > 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        return node

    def rotateLeft(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node

        node.balanceFactor = self.getHeight(node.right) - self.getHeight(node.left)
        newRoot.balanceFactor = self.getHeight(newRoot.right) - self.getHeight(newRoot.left)

        return newRoot

    def rotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node

        node.balanceFactor = self.getHeight(node.right) - self.getHeight(node.left)
        newRoot.balanceFactor = self.getHeight(newRoot.right) - self.getHeight(newRoot.left)

        return newRoot

    def getHeight(self, node):
        if not node:
            return -1
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

# Test the AVL Tree Display
avlTree = AvlTree()
avlTree.insert(10)
avlTree.insert(20)
avlTree.insert(30)

avlTreeDisplay = AvlTreeDisplay(avlTree)
