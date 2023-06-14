# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(The kth the smallest element) You can find the kth the smallest element in a BST in
O(n) time from an inorder iterator. For an AVL tree, you can find it in O(log n)
time. To achieve this, add a new data field named size in AVLTreeNode to
store the number of nodes in the subtree rooted at this node. Note that the size of
a node v is one more than the sum of the sizes of its two children. Figure 20.11
shows an AVL tree and the size value for each node in the tree.

In the AVLTree class, add the following method to return the kth the smallest element
in the tree.'''

from AVLTree import AVLTree
def main():
    avlTree = AVLTree()

    # Insert values into the AVLTree

    k = 3
    kthSmallest = avlTree.kthSmallest(k)
    if kthSmallest is not None:
        print(f"The {k}th smallest element in the AVLTree is: {kthSmallest}")
    else:
        print(f"The AVLTree does not have a {k}th smallest element.")

main()