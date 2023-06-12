class BinaryTree:
    def __init__(self):
        self.root = None

    # Method to insert a value into the binary tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertRecursive(value, self.root)

    # Recursive helper method for inserting a value into the binary tree
    def _insertRecursive(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insertRecursive(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insertRecursive(value, node.right)

    # Method to search for a value in the binary tree
    def search(self, value):
        return self._searchRecursive(value, self.root)

    # Recursive helper method for searching a value in the binary tree
    def _searchRecursive(self, value, node):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._searchRecursive(value, node.left)
        else:
            return self._searchRecursive(value, node.right)

    # Method to delete a value from the binary tree
    def delete(self, value):
        self.root = self._deleteRecursive(value, self.root)

    # Recursive helper method for deleting a value from the binary tree
    def _deleteRecursive(self, value, node):
        if node is None:
            return node

        if value < node.value:
            node.left = self._deleteRecursive(value, node.left)
        elif value > node.value:
            node.right = self._deleteRecursive(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node has two children, find the minimum value in the right subtree
            minRight = self._findMin(node.right)
            node.value = minRight.value
            node.right = self._deleteRecursive(minRight.value, node.right)

        return node

    # Helper method to find the minimum value in a subtree
    def _findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Method to get the values of the binary tree in-order traversal
    def getValuesInOrder(self):
        values = []
        self._inOrderRecursive(self.root, values)
        return values

    # Recursive helper method for in-order traversal
    def _inOrderRecursive(self, node, values):
        if node is not None:
            self._inOrderRecursive(node.left, values)
            values.append(node.value)
            self._inOrderRecursive(node.right, values)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
