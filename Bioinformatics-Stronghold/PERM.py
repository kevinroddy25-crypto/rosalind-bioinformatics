# Problem 19: Enumerating Gene Orders.

# Given a positive integer n ≤ 7.
# Return the total number of permutations of length n,
# Followed by a list of all such permutations.
import math
import itertools

n = int(input("Enter a positive integer n ≤ 7: "))

# 1. Find and print number of permutations.
# Number of permutations = n!.
num_permutations = math.factorial(n)
print(num_permutations)

# 2. Find permutations with the itertools permutations tool.
number_range = range(1, n + 1)

permutations = itertools.permutations(number_range)

# 3. Format and print all permutations.
for permutation in permutations:
    p = str(permutation).strip('()').split()
    new_p = []
    for num in p:
        new_p.append(num.replace(',', ''))
    
    print(' '.join(new_p))
