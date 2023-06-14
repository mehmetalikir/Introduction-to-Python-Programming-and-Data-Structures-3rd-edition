class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLTreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self._getBalance(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotateRight(node)
            else:
                node.left = self._rotateLeft(node.left)
                return self._rotateRight(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotateLeft(node)
            else:
                node.right = self._rotateRight(node.right)
                return self._rotateLeft(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._getMinValueNode(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self._getBalance(node)

        if balance > 1:
            if self._getBalance(node.left) < 0:
                node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        if balance < -1:
            if self._getBalance(node.right) > 0:
                node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def isAVLTree(self):
        return self._isAVLTree(self.root)

    def _isAVLTree(self, node):
        if node is None:
            return True

        if not self._isBalanced(node):
            return False

        return self._isAVLTree(node.left) and self._isAVLTree(node.right)

    def _isBalanced(self, node):
        balance = self._getBalance(node)
        return abs(balance) <= 1

    def _getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def _getBalance(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _getMinValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
