# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Maximum consecutive increasingly ordered substring) Write a program that
prompts the user to enter a string and displays the maximum consecutive
increasingly ordered substring. Analyze the time complexity of your program.'''

def main():
    s = input("Please enter a string: ")
    print("Maximum consecutive subsequence increasingly ordered substring is " + maxSubstring(s))

# The worst-case complexity is O(n^2)
def maxSubstring(s):
    stringLength = len(s)

    # maxLength[i] stores the length of the max substring ending at index i
    maxLength = stringLength * [0]
    # previous[i] stores the index of the previous element in the sequence
    previous = stringLength * [0]

    for i in range(len(s)):
        previous[i] = -1
        for j in range(i - 1, -1, -1):
            if s[i] < s[j] and maxLength[i] < maxLength[j] + 1:
                maxLength[i] = maxLength[j] + 1
                previous[i] = j

    # Find the largest subsequence length and ending index
    maxL = maxLength[0]
    index = 0
    for i in range(1, len(s)):
        if maxL < maxLength[i]:
            maxL = maxLength[i]
            index = i

    # Construct the subsequence by tracing through previous
    i = maxL
    result = ""
    while index != -1:
        result = s[index] + result
        i -= 1
        index = previous[index]

    return result


main()