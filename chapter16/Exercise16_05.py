# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Same-number subsequence) Write an O(n) program that prompts the user to
enter a sequence of integers ending with 0 and finds the longest subsequence
with the same number'''


def sameNumberSubsequence(sequence):
    longestSubsequenceStart = 0
    longestSubsequenceLength = 0

    currentStart = 0
    currentLength = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            currentLength += 1
        else:
            if currentLength > longestSubsequenceLength:
                longestSubsequenceStart = currentStart
                longestSubsequenceLength = currentLength

            currentStart = i
            currentLength = 1

    # Check the last subsequence after the loop ends
    if currentLength > longestSubsequenceLength:
        longestSubsequenceStart = currentStart
        longestSubsequenceLength = currentLength

    return longestSubsequenceStart, longestSubsequenceLength


# Prompt the user to enter the sequence
sequence = input("Please enter numbers separated by spaces from one line ending with 0: ").split()
sequence = list(map(int, sequence))

# Find the longest subsequence with the same number
startIndex, length = sameNumberSubsequence(sequence)

print("The longest same number subsequence starts at index", startIndex, "with", length, "values of",
      sequence[startIndex])
