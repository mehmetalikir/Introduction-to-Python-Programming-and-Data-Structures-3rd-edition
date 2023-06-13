# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create a binary search tree of strings) The text file JackAndJill.txt contains the
first part of the nursery rhyme Jack and Jill. Write a program that reads in the
nursery rhyme from the file and uses the BST class to create a binary search tree
with it. All words should be stored in lowercase, so every word is only included
once. When your program has created the tree, print its size.'''

from BST import BST

def createBSTFromFile(filename):
    tree = BST()
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                tree.insert(word)
    return tree

filename = "JackAndJill.txt"
tree = createBSTFromFile(filename)
print("The size of the tree is:", tree.getSize())
