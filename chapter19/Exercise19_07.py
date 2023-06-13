# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Find the nonleaves) Define a new class naed MyBST that extends BST with the
following method:

        # Return the number of nonleaf nodes
        def getNumberOfNonLeaves(self):'''


class BST:
    # Returns the number of leaf nodes
    def getNumberOfLeaves(self):
        return self.getNumberOfLeaves1(self.root)

    # Returns the number of leaf nodes
    def getNumberOfLeaves1(self, root):
        if root == None:
            return 0
        elif root.left == None or root.right == None:
            return 1
        else:
            return self.getNumberOfLeaves1(root.left) + self.getNumberOfLeaves1(root.right)

    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, e):
        return self.searchHelper(self.root, e)  # Start from the root

    def searchHelper(self, current, e):  # Search from the current subtree
        if current == None:
            return False
        elif e < current.element:
            return self.searchHelper(current.left, e)
        elif e == current.element:
            return True
        else:
            return self.searchHelper(current.right, e)

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

    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end=" ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end=" ")

    # Preorder traversal from the root
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end=" ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element
    def path(self, e):
        list = []
        current = self.root  # Start from the root

        while current != None:
            list.append(current)  # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list  # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree
    def delete(self, e):
        # Locate the node to be deleted and its parent node
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
                break  # Element is in the tree pointed by current

        if current == None:
            return False  # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right  # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left

        self.size -= 1
        return True  # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None

class MyBST(BST):
    def __init__(self):
        BST.__init__(self)

    # Returns the number of nonleaf nodes
    def getNumberOfNonLeaves(self):
        return self.size - self.getNumberOfLeaves()

    # Returns the number of leaf nodes
    def getNumberOfLeaves(self):
        return self.getNumberOfLeaves1(self.root)

    # Helper method to calculate the number of leaf nodes
    def getNumberOfLeaves1(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return self.getNumberOfLeaves1(root.left) + self.getNumberOfLeaves1(root.right)

def main():
    tree = MyBST()
    print("The number of nonleaves in an empty tree is", tree.getNumberOfNonLeaves())

    s = input("Enter integers in one line for tree separated by space: ")
    lst = [int(x) for x in s.split()]
    for e in lst:
        tree.insert(e)

    print(s, "are inserted into the tree")
    print("The number of nonleaves in the tree is", tree.getNumberOfNonLeaves())

main()
