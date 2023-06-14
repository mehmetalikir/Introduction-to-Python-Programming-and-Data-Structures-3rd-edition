# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compare performance) Write a test program that randomly generates 500,000
numbers and inserts them into a BST, reshuffles the 500,000 numbers and performs
a search, and reshuffles the numbers again before deleting them from
the tree. Write another test program that does the same thing for an AVLTree.
Compare the execution times of these two programs.'''

import random
import time
from BST import BST
from AVLTree import AVLTree


def testBst():
    bst = BST()

    # Generate and insert 500,000 random numbers
    numbers = list(range(500000))
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        bst.insert(num)
    insertionTime = time.time() - startTime

    # Reshuffle the numbers and perform a search
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        bst.search(num)
    searchTime = time.time() - startTime

    # Reshuffle the numbers and delete them from the tree
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        bst.delete(num)
    deletionTime = time.time() - startTime

    print("BST:")
    print("Insertion time:", insertionTime)
    print("Search time:", searchTime)
    print("Deletion time:", deletionTime)


def testAvlTree():
    avlTree = AVLTree()

    # Generate and insert 500,000 random numbers
    numbers = list(range(500000))
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        avlTree.insert(num)
    insertionTime = time.time() - startTime

    # Reshuffle the numbers and perform a search
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        avlTree.search(num)
    searchTime = time.time() - startTime

    # Reshuffle the numbers and delete them from the tree
    random.shuffle(numbers)

    startTime = time.time()
    for num in numbers:
        avlTree.delete(num)
    deletionTime = time.time() - startTime

    print("AVL Tree:")
    print("Insertion time:", insertionTime)
    print("Search time:", searchTime)
    print("Deletion time:", deletionTime)


# Test the performance of BST
testBst()

# Test the performance of AVL tree
testAvlTree()
