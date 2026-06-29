# Problem 29: Enumerating Oriented Gene Orderings.
# Models number of oriented rearrangements and all oriented rearrangements of a genome comprising n synteny blocks.
# At a small, easily calculable scale.

# Given a postiive integer n.
# Return the total number of signed permutations of length n,
# Followed by a list of all such permutations.

# Num permutations = n!

import itertools
import math

# 1. Define function to get the number of signed permutations of a given length n.
def get_num_permutations(n: int) -> int:
    # The number of signed perms of length n = 2^n * n!
    # B/c for each element in the perm, there are two choices.

    num_permutations = 2 ** n * math.factorial(n)
    return num_permutations

# 2. Define function to check whether a given permutation has no repeats (ignoring sign).
def has_no_repeats(permutation):
    seen = set()
    for num in permutation:
        if math.fabs(num) in seen:
            return False
        seen.add(math.fabs(num))
    return True

# 3. Define function to get all signed permutations of length n.
def get_permutations(n: int) -> str:

    # a. All possible integers = range(-n, n) with omission of 0.
    possible_integers = [integer for integer in list(range(-n, n + 1)) if integer != 0]

    # b. Get permutations with itertools.
    permutations_tuple = itertools.permutations(possible_integers, n)
    permutations_list = []
    # Check to ensure no pos/neg integer repeats.
    for permutation in permutations_tuple:
        if has_no_repeats(permutation):
            permutations_list.append(' '.join(str(x) for x in permutation))

    # c. Format and return all permutations.
    permutations = '\n'.join(permutations_list)
    return permutations

# 4. Ask for input.
n = int(input('Enter a positive integer n ≤ 6: '))

# 5. Execute and print results.
print(get_num_permutations(n))
print(get_permutations(n))
