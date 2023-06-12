# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Postfix notation) Postfix notation is a way of writing expressions without using
parentheses. For example, the expression (1 + 2) * 3 would be written as 1 2 + 3 *.
A postfix expression is evaluated using a stack. Scan a postfix expression from
left to right. A variable or constant is pushed to the stack. When an operator is
encountered, apply the operator with two top operands in the stack and replace the
two operands with result. The following diagram shows how to evaluate 12 + 3 *.

Write a program that prompts the user to enter a postfix expression and evaluate it.'''

class Stack:
    def __init__(self):
        self.__elements = []

    def isEmpty(self):
        return len(self.__elements) == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)


def main():
    expression = input("Please enter a postfix expression: ").strip() # 5 1 + 8 * 3 -
    try:
        print(expression, "=", evaluateExpression(expression))
    except:
        print("Wrong expression:", expression)


def evaluateExpression(expression):
    operandStack = Stack()

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            operandStack.push(float(token))
        elif token == "+":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operand1 + operand2
            operandStack.push(result)
        elif token == "-":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operand1 - operand2
            operandStack.push(result)
        elif token == "*":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operand1 * operand2
            operandStack.push(result)
        elif token == "/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = operand1 / operand2
            operandStack.push(result)

    return operandStack.pop()


main()


