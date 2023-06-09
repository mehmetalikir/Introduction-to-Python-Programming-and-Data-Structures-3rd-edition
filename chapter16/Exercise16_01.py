# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Maximum consecutive increasingly ordered substring) Write a program that
prompts the user to enter a string and displays the maximum consecutive
increasingly ordered substring. Analyze the time complexity of your program.'''

def main():
    s = input("Please enter a string: ")
    print("Maximum consecutive increasingly ordered substring is " + maxSubstring(s))

def maxSubstring(s):
    # Check if the input string is empty
    if len(s) == 0:
        return ""

    # Initialize variables to track the maximum and current substrings
    max_substring = ""
    current_substring = s[0]

    # Iterate through the input string
    for i in range(1, len(s)):
        # Check if the current character is greater than or equal to the previous character
        if ord(s[i]) >= ord(s[i-1]):
            # If so, add the current character to the current substring
            current_substring += s[i]
        else:
            # If not, compare the length of the current substring with the maximum substring
            if len(current_substring) > len(max_substring):
                # Update the maximum substring if necessary
                max_substring = current_substring
            # Reset the current substring to the current character
            current_substring = s[i]

    # Check the last current substring after the loop ends
    if len(current_substring) > len(max_substring):
        max_substring = current_substring

    return max_substring


main()
