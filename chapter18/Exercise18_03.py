# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement LinkedList) The implementations of methods remove(e),
indexOf(e), and set(index,e) are omitted in the text. Implement these methods.
Use https://liangpy.pearsoncmg.com/test/Exercise18_03.txt to test your code'''


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element

    # Return the last element in the list
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list
    def addFirst(self, e):
        newNode = Node(e)  # Create a new node
        newNode.next = self.__head  # link the new node with the head
        self.__head = newNode  # head points to the new node
        self.__size += 1  # Increase list size

        if self.__tail == None:  # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list
    def addLast(self, e):
        newNode = Node(e)  # Create a new node for e

        if self.__tail == None:
            self.__head = self.__tail = newNode  # The only node in list
        else:
            self.__tail.next = newNode  # Link the new with the last node
            self.__tail = self.__tail.next  # tail now points to the last node

        self.__size += 1  # Increase size

    # Same as addLast
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)  # Insert first
        elif index >= self.__size:
            self.addLast(e)  # Insert last
        else:  # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node.
    def removeFirst(self):
        if self.__size == 0:
            return None  # Nothing to delete
        else:
            temp = self.__head  # Keep the first node temporarily
            self.__head = self.__head.next  # Move head to point the next node
            self.__size -= 1  # Reduce size by 1
            if self.__head == None:
                self.__tail = None  # List becomes empty
            return temp.element  # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None  # Nothing to remove
        elif self.__size == 1:  # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head

            for i in range(self.__size - 2):
                current = current.next

            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list.
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None  # Out of range
        elif index == 0:
            return self.removeFirst()  # Remove first
        elif index == self.__size - 1:
            return self.removeLast()  # Remove last
        else:
            previous = self.__head

            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next
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
