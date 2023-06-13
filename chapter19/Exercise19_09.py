# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Add new buttons in BSTAnimation) Modify Listing 19.7, BSTAnimation.py,
to add three new buttons—Show Inorder, Show Preorder, and Show Postorder—
to display the result in a message box, as shown in Figure 19.20. You need
to add the following methods in the BST class to return a list of node elements
in inorder, preorder, and postorder:

    def inorderList(self):
    def preorderList(self):
    def postorderList(self):

When you click the Show Inorder button in (a),the tree nodes are displayed
in an inorder in a message dialog box in (b).'''

import tkinter.messagebox
from tkinter import *

from BST import BST
from BTView import BTView


class BSTAnimation:
    def __init__(self, tree):
        window = Tk()  # Create a window
        window.title("BSTAnimation")  # Set a title

        self.width = 200
        self.height = 200
        self.radius = 20
        self.v_gap = 50
        self.tree = tree
        self.view = BTView(tree, window, self.width, self.height, self.radius, self.v_gap)
        self.view.pack()

        frame = Frame(window)  # Create and add a frame to window
        frame.pack()

        Label(frame, text="Please enter a key").pack(side=LEFT)
        self.key = StringVar()
        Entry(frame, textvariable=self.key, justify=RIGHT).pack(side=LEFT)
        Button(frame, text="Insert", command=self.insert).pack(side=LEFT)
        Button(frame, text="Delete", command=self.delete).pack(side=LEFT)

        # Add the Show Inorder button
        Button(frame, text="Show Inorder", command=self.showInorder).pack(side=LEFT)
        # Add the Show Preorder button
        Button(frame, text="Show Preorder", command=self.showPreorder).pack(side=LEFT)
        # Add the Show Postorder button
        Button(frame, text="Show Postorder", command=self.showPostorder).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def insert(self):
        key = int(self.key.get())
        if self.tree.search(key):  # Key is already in the tree
            tkinter.messagebox.showinfo("Insertion Status", str(key) + " is already in the tree")
        else:
            self.tree.insert(key)  # Insert a new key
            self.view.delete("tree")
            self.view.displayTree(self.tree.getRoot(), self.width / 2, 30, self.width / 4)

    def delete(self):
        key = int(self.key.get())
        if not self.tree.search(key):  # Key is not in the tree
            tkinter.messagebox.showinfo("Deletion Status", str(key) + " is not in the tree")
        else:
            self.tree.delete(key)  # Delete the key
            self.view.delete("tree")
            self.view.displayTree(self.tree.getRoot(), self.width / 2, 30, self.width / 4)

    def showInorder(self):
        inorder_list = self.tree.inorderList()
        message = "Inorder traversal: " + " ".join(map(str, inorder_list))
        tkinter.messagebox.showinfo("Inorder Traversal", message)

    def showPreorder(self):
        preorder_list = self.tree.preorderList()
        message = "Preorder traversal: " + " ".join(map(str, preorder_list))
        tkinter.messagebox.showinfo("Preorder Traversal", message)

    def showPostorder(self):
        postorder_list = self.tree.postorderList()
        message = "Postorder traversal: " + " ".join(map(str, postorder_list))
        tkinter.messagebox.showinfo("Postorder Traversal", message)


BSTAnimation(BST())
