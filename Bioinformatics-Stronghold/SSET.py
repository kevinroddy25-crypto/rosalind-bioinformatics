# Problem 43: Counting Subsets.

# Given a positive integer n.
# Return the total number of subsets of {1, 2, ..., n} modulo 10^6.

from math import comb

# 1. Define a function to get the number of possible subsets from a given set.
def get_num_subsets(n: int):
    # The number of subsets of length i from a set of length n
    # can be found with the combination formula.
    num_subsets = 1 # ∅ is always a subset of any set
    for i in range(1, n + 1):
        num_subsets += comb(n, i)

    return num_subsets % 1000000

# 2. Get n as input.
n = int(input('Enter a positive integer n: '))

# 3. Execute and print results.
print(get_num_subsets(n))
