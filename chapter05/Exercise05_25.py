# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, mehmetalikir@outlook.com
# GitHub: /hidirsezgin, /mehmetalikir

'''(Demonstrate cancellation errors) A cancellation error occurs when you are
manipulating a very large number with a very small number. The large number
may cancel out the smaller number. For example, the result of 100000000.0 +
0.000000001 is equal to 100000000.0. To avoid cancellation errors and obtain
more accurate results, carefully select the order of computation. For example, in
computing the following series, you will obtain more accurate results by computing
from right to left rather than from left to right:

Write a program that compares the results of the summation of the preceding
series, computing from left to right and from right to left with n = 50000.'''

# Constant
N = 50_000


result = 1
# Display result
for i in range(N, 1, -1):
    result += 1 / i
print("Result: ", result)
