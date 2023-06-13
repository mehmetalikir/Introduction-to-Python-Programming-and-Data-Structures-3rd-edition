from tkinter import *  # Import tkinter


class BTView(Canvas):
    # Construct a view for the tree
    def __init__(self, tree, container, width, height, radius, vGap):
        super().__init__(container, width=width, height=height)
        self.tree = tree
        self.radius = radius
        self.vGap = vGap

    # Display a subtree rooted at position (x, y)
    def displayTree(self, root, x, y, hGap):
        if root == None: return  # Empty tree

        # Display the root
        self.create_oval(x - self.radius, y - self.radius,
                         x + self.radius, y + self.radius, tags="tree")
        self.create_text(x, y,
                         text=str(root.element), tags="tree")

        if root.left != None:
            # Draw a line to the left node
            self.connectTwoCircles(x - hGap, y + self.vGap, x, y)
            # Draw the left subtree recursively
            self.displayTree(root.left, x - hGap, y
                             + self.vGap, hGap / 2)

        if root.right != None:
            # Draw a line to the right node
            self.connectTwoCircles(x + hGap, y + self.vGap, x, y)
            # Draw the right subtree recursively
            self.displayTree(root.right, x + hGap, y
                             + self.vGap, hGap / 2)

    # Connect two circles centered at (x1, y1) and (x2, y2)
    def connectTwoCircles(self, x1, y1, x2, y2):
        d = (self.vGap * self.vGap + (x2 - x1) * (x2 - x1)) ** 0.5
        x11 = x1 - self.radius * (x1 - x2) / d
        y11 = y1 - self.radius * (y1 - y2) / d
        x21 = x2 + self.radius * (x1 - x2) / d
        y21 = y2 + self.radius * (y1 - y2) / d
        self.create_line(x11, y11, x21, y21, tags="tree")
