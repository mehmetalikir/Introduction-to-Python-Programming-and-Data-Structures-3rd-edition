# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Animate linear probing) Write a program that animates linear probing. You
can change the initial size of the hash table. Assume the load-factor threshold is
0.75'''

import time
import tkinter as tk

# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 10

# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.75


class HashTable:
    def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR):
        self.capacity = capacity
        self.loadFactorThreshold = loadFactorThreshold
        self.table = [None] * self.capacity
        self.size = 0

    def hashFunction(self, key):
        return key % self.capacity

    def insert(self, key):
        index = self.hashFunction(key)
        while self.table[index] is not None:
            index = (index + 1) % self.capacity

        self.table[index] = key
        self.size += 1

    def rehash(self):
        oldTable = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for key in oldTable:
            if key is not None:
                self.insert(key)


class AnimationWindow:
    def __init__(self, hashTable):
        self.hashTable = hashTable
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()
        self.delay = 500  # Animation delay in milliseconds

    def animate_insertion(self, key):
        index = self.hashTable.hashFunction(key)
        while self.hashTable.table[index] is not None:
            index = (index + 1) % self.hashTable.capacity

        self.canvas.create_text(index * 50 + 30, 200, text=str(key), font=("Arial", 12), fill="black")
        self.canvas.update()
        time.sleep(self.delay / 1000)  # Delay for animation effect
        self.hashTable.table[index] = key

    def animate_rehash(self):
        self.canvas.delete("all")
        self.canvas.create_text(300, 200, text="Rehashing...", font=("Arial", 16), fill="red")
        self.canvas.update()
        time.sleep(self.delay / 1000)  # Delay for animation effect
        self.hashTable.rehash()
        self.canvas.delete("all")
        self.draw_hash_table()

    def draw_hash_table(self):
        for i in range(self.hashTable.capacity):
            if self.hashTable.table[i] is not None:
                self.canvas.create_text(i * 50 + 30, 200, text=str(self.hashTable.table[i]), font=("Arial", 12),
                                        fill="black")
        self.canvas.update()

    def run(self):
        self.window.title("Linear Probing Animation")
        self.draw_hash_table()

        keys = [23, 45, 12, 78, 56, 89, 34, 67, 90, 43]
        for key in keys:
            self.animate_insertion(key)
            if self.hashTable.size >= self.hashTable.capacity * self.hashTable.loadFactorThreshold:
                self.animate_rehash()

        self.window.mainloop()


def main():
    # Create a hash table
    hashTable = HashTable()

    # Create the animation window and run the animation
    animationWindow = AnimationWindow(hashTable)
    animationWindow.run()


main()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define the default hash-table size
# DEFAULT_INITIAL_CAPACITY = 10
#
# # Define default load factor
# DEFAULT_MAX_LOAD_FACTOR = 0.75
#
#
# class HashTable:
#     def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR):
#         self.capacity = capacity
#         self.loadFactorThreshold = loadFactorThreshold
#         self.table = [None] * self.capacity
#         self.size = 0
#         self.convert_yunits = None
#         self._y0 = 1
#         self._height = 0
#
#     def hashFunction(self, key):
#         return key % self.capacity
#
#     def insert(self, key):
#         if self.size >= self.capacity * self.loadFactorThreshold:
#             self.rehash(key)
#
#         index = self.hashFunction(key)
#         while self.table[index] is not None:
#             index = (index + 1) % self.capacity
#
#         self.table[index] = key
#         self.size += 1
#
#     def rehash(self, key):
#         oldTable = self.table
#         self.capacity *= 2
#         self.table = [None] * self.capacity
#         self.size = 0
#
#         for key in oldTable:
#             if key is not None:
#                 self.insert(key)
#
#     def visualize(self):
#         if self.convert_yunits is not None and self._y0 is not None and self._height is not None:
#             plt.figure()
#             plt.title('Linear Probing')
#             plt.xlabel('Index')
#             plt.ylabel('Value')
#
#             indices = np.arange(self.capacity)
#             values = np.array(self.table)
#
#             plt.bar(indices, values)
#
#             # Perform the conversion of y0 and height using convert_yunits
#             y0 = self.convert_yunits(self._y0) if self._y0 is not None else 0
#             height = self.convert_yunits(self._height) if self._height is not None else 0
#
#             # Set the y-axis limits based on the converted y0 and height
#             plt.ylim(y0, y0 + height)
#
#             plt.show()
#         else:
#             print("Missing conversion function or y0 or height value")
#
#
# def main():
#     # Create a hash table
#     hashTable = HashTable()
#
#     # Insert keys into the hash table
#     keys = [23, 45, 12, 78, 56, 89, 34, 67, 90, 43]
#     for key in keys:
#         hashTable.insert(key)
#
#     # Visualize the hash table
#     hashTable.visualize()
#
#
# main()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define the default hash-table size
# DEFAULT_INITIAL_CAPACITY = 10
#
# # Define default load factor
# DEFAULT_MAX_LOAD_FACTOR = 0.75
#
#
# class HashTable:
#     def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR):
#         self.capacity = capacity
#         self.loadFactorThreshold = loadFactorThreshold
#         self.table = [None] * self.capacity
#         self.size = 0
#         self.convert_yunits = None
#         self._y0 = 1
#         self._height = 0
#
#     def hashFunction(self, key):
#         return key % self.capacity
#
#     def insert(self, key):
#         if self.size >= self.capacity * self.loadFactorThreshold:
#             self.rehash(key)
#
#         index = self.hashFunction(key)
#         while self.table[index] is not None:
#             index = (index + 1) % self.capacity
#
#         self.table[index] = key
#         self.size += 1
#
#     def rehash(self, key):
#         oldTable = self.table
#         self.capacity *= 2
#         self.table = [None] * self.capacity
#         self.size = 0
#
#         for key in oldTable:
#             if key is not None:
#                 self.insert(key)
#
#     def visualize(self):
#         if self.convert_yunits is not None and self._y0 is not None and self._height is not None:
#             plt.figure()
#             plt.title('Linear Probing')
#             plt.xlabel('Index')
#             plt.ylabel('Value')
#
#             indices = np.arange(self.capacity)
#             values = np.array(self.table)
#
#             plt.bar(indices, values)
#
#             # Perform the conversion of y0 and height using convert_yunits
#             y0 = self.convert_yunits(self._y0) if self._y0 is not None else 0
#             height = self.convert_yunits(self._height) if self._height is not None else 0
#
#             # Set the y-axis limits based on the converted y0 and height
#             plt.ylim(y0, y0 + height)
#
#             plt.show()
#         else:
#             print("Missing conversion function or y0 or height value")
#
#
# def main():
#     # Create a hash table
#     hashTable = HashTable()
#
#     # Insert keys into the hash table
#     keys = [23, 45, 12, 78, 56, 89, 34, 67, 90, 43]
#     for key in keys:
#         hashTable.insert(key)
#
#     # Visualize the hash table
#     hashTable.visualize()
#
#
# main()
