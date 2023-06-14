# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Test AVLTree) Add the method isAVLTree to the BST class to determine if the
tree is an AVL tree.

    # Returns true if the tree is an AVL tree
    def isAVLTree(self):

Also, using the method created for Programing Exercise 20.6'''

# Create an instance of the BST class
from BST import BST
bst = BST()

# Insert nodes to construct the binary search tree
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(12)
bst.insert(18)

# Check if the tree is an AVL tree
isAvl = bst.isAVLTree()

# Print the result
if isAvl:
    print("The tree is an AVL tree.")
else:
    print("The tree is not an AVL tree.")

