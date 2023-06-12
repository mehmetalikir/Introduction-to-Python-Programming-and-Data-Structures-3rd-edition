# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Animation: Linked list) Write a program to animate search, insertion, and deletion
in a linked list. The Search button searches whether the specified
value is in the list. The Delete button deletes the specified value from the list. The
Insert button inserts the value into the list if the index is not specified; otherwise,
it inserts the value into the specified index in the list.'''

import tkinter as tk


# Define the Node class for linked list nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a value at the end of the list
    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    # Method to search for a value in the list
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    # Method to delete a value from the list
    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    # Method to get the values in the list as a string
    def getValues(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values)


# Create the tkinter GUI
root = tk.Tk()
root.title("Linked List Animation")

# Create a LinkedList object
linkedList = LinkedList()


# Function to update the linked list display
def updateDisplay():
    display.config(text=linkedList.getValues())


# Function to perform a search operation
def searchOperation():
    value = int(valueEntry.get())
    if linkedList.search(value):
        operationLabel.config(text="Value found!")
    else:
        operationLabel.config(text="Value not found!")


# Function to perform an insertion operation
def insertOperation():
    value = int(valueEntry.get())
    index = int(indexEntry.get())

    if index < 0 or index > len(linkedList.getValues()):
        operationLabel.config(text="Invalid index!")
        return

    linkedList.insert(value)
    updateDisplay()
    operationLabel.config(text="Value inserted at index {}".format(index))


# Function to perform a deletion operation
def deleteOperation():
    value = int(valueEntry.get())
    linkedList.delete(value)
    updateDisplay()
    operationLabel.config(text="Value deleted")


# Create GUI components
display = tk.Label(root, text="", font=("Arial", 16))
display.pack(pady=10)

valueLabel = tk.Label(root, text="Value:")
valueLabel.pack()
valueEntry = tk.Entry(root)
valueEntry.pack()

indexLabel = tk.Label(root, text="Index:")
indexLabel.pack()
indexEntry = tk.Entry(root)
indexEntry.pack()

searchButton = tk.Button(root, text="Search", command=searchOperation)
searchButton.pack(pady=5)

insertButton = tk.Button(root, text="Insert", command=insertOperation)
insertButton.pack(pady=5)

deleteButton = tk.Button(root, text="Delete", command=deleteOperation)
deleteButton.pack(pady=5)

operationLabel = tk.Label(root, text="")
operationLabel.pack()

# Start the GUI event loop
root.mainloop()
