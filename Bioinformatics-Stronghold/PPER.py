# Problem 27: Partial Permutations.

# P(n,n) = n!
# P(n,k) = n! / (n - k)!

# Given positive integers n and k.
# Return the total number of partial permutations P(n,k) % 10^6.

import math

# 1. Define function to get number of partial permutations using math.perm.
def get_num_partial_permutations(n: int, k: int) -> int:
    
    # math.perm(n, k) directly calculates n! / (n - k)!
    total_permutations = math.perm(n, k)

    return total_permutations % 1000000

# 2. Ask for input, execute function, and print output.
n, k = map(int, input('Enter integers n and k: ').split(' '))
print(get_num_partial_permutations(n, k))
