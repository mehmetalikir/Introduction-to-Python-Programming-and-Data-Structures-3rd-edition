# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create a doubly linked list) The LinkedList class used in Listing 18.2
is a singly linked list that enables one-way traversal of the list.
Modify the Node class to add the new data field name previous to refer to the
previous node in the list, as follows:

class Node:
    def Note(self, e):
        self.element = e
        self.previous = None
        self.next = None
Implement a new class named TwoWayLinkedList that uses a doubly-linked
list to store elements.'''


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element

    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    def addFirst(self, e):
        newNode = Node(e)
        newNode.next = self.__head

        if self.__head is not None:
            self.__head.previous = newNode

        self.__head = newNode

        if self.__tail is None:
            self.__tail = self.__head

        self.__size += 1

    def addLast(self, e):
        newNode = Node(e)

        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            newNode.previous = self.__tail
            self.__tail.next = newNode
            self.__tail = newNode

        self.__size += 1

    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(index):
                current = current.next

            temp = current.previous
            newNode = Node(e)
            newNode.previous = temp
            newNode.next = current
            current.previous = newNode
            temp.next = newNode

            self.__size += 1

    def removeFirst(self):
        if self.__size == 0:
            return None
        else:
            temp = self.__head
            self.__head = self.__head.next
            if self.__head is not None:
                self.__head.previous = None
            else:
                self.__tail = None

            self.__size -= 1
            return temp.element

    def removeLast(self):
        if self.__size == 0:
            return None
        else:
            temp = self.__tail
            self.__tail = self.__tail.previous
            if self.__tail is not None:
                self.__tail.next = None
            else:
                self.__head = None

            self.__size -= 1
            return temp.element

    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None
        elif index == 0:
            return self.removeFirst()
        elif index == self.__size - 1:
            return self.removeLast()
        else:
            current = self.__head
            for i in range(index):
                current = current.next

            current.previous.next = current.next
            current.next.previous = current.previous

            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0

    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", "  # Separate two elements with a comma
            else:
                result += "]"  # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element e
    def contains(self, e):
        current = self.__head
        while current is not None:
            if current.element == e:
                return True
            current = current.next
        return False

    # Remove the element e from the list and return True if the element is found
    def remove(self, e):
        if self.__head is None:
            return False

        if self.__head.element == e:
            self.removeFirst()
            return True

        previous = self.__head
        current = self.__head.next
        while current is not None:
            if current.element == e:
                previous.next = current.next
                if current == self.__tail:
                    self.__tail = previous
                self.__size -= 1
                return True
            previous = current
            current = current.next

        return False

    # Return the element at the specified index in this list
    def get(self, index):
        if index < 0 or index >= self.__size:
            return None

        current = self.__head
        for i in range(index):
            current = current.next
        return current.element

    # Return the index of the first occurrence of the element e in this list
    # Return -1 if the element is not found
    def indexOf(self, e):
        current = self.__head
        index = 0
        while current is not None:
            if current.element == e:
                return index
            current = current.next
            index += 1
        return -1

    # Return the index of the last occurrence of the element e in this list
    # Return -1 if the element is not found
    def lastIndexOf(self, e):
        current = self.__head
        lastIndex = -1
        index = 0
        while current is not None:
            if current.element == e:
                lastIndex = index
            current = current.next
            index += 1
        return lastIndex

    # Replace the element at the specified position in this list with the specified element
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return None

        current = self.__head
        for i in range(index):
            current = current.next
        current.element = e
    def add(self, e):
        self.addLast(e)

    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)


# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.previous = None
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element


def main():
    lista = input("Please enter list1: ").split()
    list1 = LinkedList()
    for s in lista:
        list1.add(s)

    print("list1.indexOf('red') is", list1.indexOf('red'))
    list1.remove("red")
    print("after invoking list1.remove('red'), list1 is", list1)
    index = int(input("Enter an index: "))
    list1.set(index, "orange")
    print("after invoking list1.set('" + str(index) + " , orange)",
          "list1 is", list1)


main()
