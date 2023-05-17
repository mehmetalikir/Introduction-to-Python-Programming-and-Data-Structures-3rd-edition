# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement Stack using inheritance) In Listing 12.13, the Stack class is
implemented using composition. Define a new Stack class using inheritance
that extends list.
Draw UML diagrams of the new class. Implement it. Write a test program that
prompts the user to enter five strings and displays them in reverse order.'''


class Stack(list):
    def __init__(self):
        super().__init__()

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self) == 0

    # Returns the element at the top of the stack
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self[-1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self[-1]
            del self[-1]
            return temp

    # Return the size of the stack
    def getSize(self):
        return len(self)


stack = Stack()

# Push from 1 to 10
for i in range(1, 11):
    stack.push(i)

while not stack.isEmpty():
    print(stack.pop())
