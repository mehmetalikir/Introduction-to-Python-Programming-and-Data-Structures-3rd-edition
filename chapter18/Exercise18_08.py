# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Convert infix to postfix) Write a function that converts an infix expression into a
postfix expression using the following header:

    def infixToPostfix(expression):

For example, the function should convert the infix expression (1+ 2) * 3 to
1 2 + 3 * and 2 * (1 + 2) to 2 1 3 + *.'''

import Stack


def main():
    expression1 = "(1 + 2) * 3"
    expression2 = "2 * (1 + 2)"

    postfix1 = infixToPostfix(expression1)
    postfix2 = infixToPostfix(expression2)

    print("Postfix expression 1:", postfix1)  # Output: 1 2 + 3 *
    print("Postfix expression 2:", postfix2)  # Output: 2 1 2 + *


def infixToPostfix(expression):
    # Create an empty stack to store operators
    operatorStack = Stack.Stack()

    # Create an empty string to store the postfix expression
    postfixExpression = ""

    # Define the precedence of operators
    precedence = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    # Iterate over each character in the expression
    for char in expression:
        # Ignore whitespace characters
        if char == ' ':
            continue

        # If the character is an operand, add it to the postfix expression
        if char.isalnum():
            postfixExpression += char
        # If the character is '(', push it to the operator stack
        elif char == '(':
            operatorStack.push(char)
        # If the character is ')', pop operators from the stack and add them to the postfix expression until '(' is
        # encountered
        elif char == ')':
            while not operatorStack.isEmpty() and operatorStack.peek() != '(':
                postfixExpression += operatorStack.pop()
            if not operatorStack.isEmpty() and operatorStack.peek() == '(':
                operatorStack.pop()
        # If the character is an operator, pop operators from the stack and add them to the postfix expression based
        # on precedence
        else:
            while not operatorStack.isEmpty() and operatorStack.peek() != '(' and precedence[char] <= precedence[
                operatorStack.peek()]:
                postfixExpression += operatorStack.pop()
            operatorStack.push(char)

    # Pop any remaining operators from the stack and add them to the postfix expression
    while not operatorStack.isEmpty():
        postfixExpression += operatorStack.pop()

    return postfixExpression


main()
