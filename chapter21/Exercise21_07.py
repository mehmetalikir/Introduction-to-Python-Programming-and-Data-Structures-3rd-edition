# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Animate separate chaining) Write a program that animates separate chaining.
You can change the initial size of the table. Assume the load-factor threshold is 0.75'''

import tkinter as tk
import time


# Define the default table size
DEFAULT_INITIAL_SIZE = 10

# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.75

# Define the animation duration (in seconds)
ANIMATION_DURATION = 0.5

class HashTableAnimation:
    def __init__(self, size=DEFAULT_INITIAL_SIZE, loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR):
        self.size = size
        self.loadFactorThreshold = loadFactorThreshold
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0

        # Initialize the tkinter window
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=400)
        self.canvas.pack()

    def hashFunction(self, key):
        return key % self.size

    def insert(self, key):
        if self.num_elements >= self.size * self.loadFactorThreshold:
            self.rehash()

        index = self.hashFunction(key)
        self.table[index].append(key)
        self.num_elements += 1

    def rehash(self):
        self.size *= 2
        new_table = [[] for _ in range(self.size)]

        for chain in self.table:
            for key in chain:
                new_index = self.hashFunction(key)
                new_table[new_index].append(key)

        self.table = new_table

    def visualize(self):
        self.canvas.delete("all")

        # Calculate the width and height of each cell in the visualization
        cell_width = 800 / self.size
        cell_height = 350 / self.size

        # Draw the cells and elements
        for i, chain in enumerate(self.table):
            for j, key in enumerate(chain):
                x0 = i * cell_width
                y0 = j * cell_height
                x1 = (i + 1) * cell_width
                y1 = (j + 1) * cell_height

                self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(key))

        self.root.update()
        time.sleep(ANIMATION_DURATION)

    def animate(self, keys):
        for key in keys:
            self.insert(key)
            self.visualize()

    def start(self):
        self.root.mainloop()


def main():
    # Create a hash table animation
    hashTableAnimation = HashTableAnimation()

    # Insert keys into the hash table animation
    keys = [23, 45, 12, 78, 56, 89, 34, 67, 90, 43]

    # Animate the separate chaining
    hashTableAnimation.animate(keys)

    # Start the tkinter event loop
    hashTableAnimation.start()



main()
