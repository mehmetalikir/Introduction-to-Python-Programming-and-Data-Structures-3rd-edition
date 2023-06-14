class BST:
    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.TreeNode(key)
        else:
            self._insertRecursive(key, self.root)

    def _insertRecursive(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = self.TreeNode(key)
            else:
                self._insertRecursive(key, node.left)
        else:
            if node.right is None:
                node.right = self.TreeNode(key)
            else:
                self._insertRecursive(key, node.right)

    def delete(self, key):
        self.root = self._deleteRecursive(key, self.root)

    def _deleteRecursive(self, key, node):
        if node is None:
            return node

        if key < node.key:
            node.left = self._deleteRecursive(key, node.left)
        elif key > node.key:
            node.right = self._deleteRecursive(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            minRight = self._findMin(node.right)
            node.key = minRight.key
            node.right = self._deleteRecursive(minRight.key, node.right)

        return node

    def search(self, key):
        return self._searchRecursive(key, self.root)

    def _searchRecursive(self, key, node):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._searchRecursive(key, node.left)
        else:
            return self._searchRecursive(key, node.right)

    def isBalanced(self):
        return self._isBalancedRecursive(self.root)

    def _isBalancedRecursive(self, node):
        if node is None:
            return True

        leftHeight = self._getHeight(node.left)
        rightHeight = self._getHeight(node.right)
        balanceFactor = abs(leftHeight - rightHeight)

        if balanceFactor > 1:
            return False

        return self._isBalancedRecursive(node.left) and self._isBalancedRecursive(node.right)

    def _getHeight(self, node):
        if node is None:
            return -1

        leftHeight = self._getHeight(node.left)
        rightHeight = self._getHeight(node.right)

        return max(leftHeight, rightHeight) + 1

    def _findMin(self, node):
        while node.left is not None:
            node = node.left

        return node
