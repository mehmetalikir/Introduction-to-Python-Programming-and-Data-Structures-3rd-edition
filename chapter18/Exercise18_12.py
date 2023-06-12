# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Animation: doubly linked list) Write a program to animate search, insertion,
and deletion in a doubly linked list, as shown in Figure 18.19a. The Search button
searches the specified value in the list. The Delete button deletes the specified
value from the list. The Insert button inserts the value into the specified
index in the list. The Forward Traversal and Backward Traversal buttons
display the elements in a message dialog box in forward and backward order,
respectively, as shown in Figure 18.19b'''

from tkinter import *
from tkinter import messagebox


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, value):
        newNode = Node(value)

        if index < 0:
            messagebox.showerror("Error", "Invalid index!")
            return

        if index == 0:
            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode
            messagebox.showinfo("Insertion", f"Inserted {value} at index {index}!")
            return

        current = self.head
        currentIndex = 0

        while currentIndex < index - 1 and current:
            current = current.next
            currentIndex += 1

        if not current:
            messagebox.showerror("Error", "Invalid index!")
            return

        newNode.next = current.next
        if current.next:
            current.next.prev = newNode
        current.next = newNode
        newNode.prev = current
        messagebox.showinfo("Insertion", f"Inserted {value} at index {index}!")

    def delete(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next

        if not current:
            messagebox.showerror("Error", f"{value} not found in the list!")
            return

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev

        messagebox.showinfo("Deletion", f"Deleted {value} from the list!")

    def search(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next

        if current:
            messagebox.showinfo("Search", f"{value} found in the list!")
        else:
            messagebox.showinfo("Search", f"{value} not found in the list!")

    def forwardTraversal(self):
        current = self.head
        result = "Forward Traversal:\n"

        while current:
            result += str(current.data) + " "
            current = current.next

        messagebox.showinfo("Forward Traversal", result)

    def backwardTraversal(self):
        current = self.head

        if not current:
            messagebox.showinfo("Backward Traversal", "The list is empty!")
            return

        while current.next:
            current = current.next

        result = "Backward Traversal:\n"

        while current:
            result += str(current.data) + " "
            current = current.prev

        messagebox.showinfo("Backward Traversal", result)


def insertValue():
    index = int(indexEntry.get())
    value = int(valueEntry.get())
    linkedList.insert(index, value)
    displayList()


def deleteValue():
    value = int(valueEntry.get())
    linkedList.delete(value)
    displayList()


def searchValue():
    value = int(valueEntry.get())
    linkedList.search(value)


def forwardTraversal():
    linkedList.forwardTraversal()


def backwardTraversal():
    linkedList.backwardTraversal()


def displayList():
    current = linkedList.head
    result = "Doubly Linked List: "

    while current:
        result += str(current.data) + " "
        current = current.next

    listLabel.config(text=result)


linkedList = DoublyLinkedList()

window = Tk()
# Rest of the code remains the same...

window.title("Doubly Linked List Animation")

titleLabel = Label(window, text="Doubly Linked List Animation", font=("Arial", 16, "bold"))
titleLabel.pack(pady=10)

# Frame for input and buttons
inputFrame = Frame(window)
inputFrame.pack(pady=10)

indexLabel = Label(inputFrame, text="Index:")
indexLabel.grid(row=0, column=0, padx=5)

indexEntry = Entry(inputFrame, width=10)
indexEntry.grid(row=0, column=1, padx=5)

valueLabel = Label(inputFrame, text="Value:")
valueLabel.grid(row=0, column=2, padx=5)

valueEntry = Entry(inputFrame, width=10)
valueEntry.grid(row=0, column=3, padx=5)

insertButton = Button(inputFrame, text="Insert", width=10, command=insertValue)
insertButton.grid(row=0, column=4, padx=5)

deleteButton = Button(inputFrame, text="Delete", width=10, command=deleteValue)
deleteButton.grid(row=0, column=5, padx=5)

searchButton = Button(inputFrame, text="Search", width=10, command=searchValue)
searchButton.grid(row=0, column=6, padx=5)

traversalFrame = Frame(window)
traversalFrame.pack(pady=10)

forwardButton = Button(traversalFrame, text="Forward Traversal", width=15, command=forwardTraversal)
forwardButton.grid(row=0, column=0, padx=5)

backwardButton = Button(traversalFrame, text="Backward Traversal", width=15, command=backwardTraversal)
backwardButton.grid(row=0, column=1, padx=5)

listLabel = Label(window, text="Doubly Linked List: ")
listLabel.pack(pady=10)

window.mainloop()
