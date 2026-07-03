# Problem 39: Ordering Strings of Varying Length Lexicographically.
# Uses two file paths. Adjust as necessary.

# Given a permutation of symbols defining an ordered alphabet and a positive integer n.
# Return all strings of length at most n formed from the alphabet, ordered lexicographically.

import itertools

# 1. Define a function to get all strings of length at most n from alphabet A, ordered lexicographically.
def get_strings_from_alphabet(A: list, n: int) -> list:
    strings = []
    for length in range(1, n + 1):
        perms = itertools.product(A, repeat=length)
        for perm in perms:
            strings.append(''.join([symbol for symbol in perm]))
    
    lex_rankings = {symbol: idx for idx, symbol in enumerate(A)}
    # Sort by custom alphabet order; lists compare lexicographically in Python
    strings.sort(key=lambda permutation: [lex_rankings.get(symbol, len(A)) for symbol in permutation])

    return strings

# 2. Parse given file for alphabet A and integer n.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_lexv.txt'
with open(file_path, 'r') as f:
    A = f.readline().strip().split()
    n = int(f.readline().strip())

# 3. Execute and print results. Write output in a new file due to large number of permutations.
# Adjust file path as necessary.
strings = '\n'.join(get_strings_from_alphabet(A, n))

file_path = 'path/to/your/rosalind_lexv_output.txt'
with open(file_path, 'w') as f:
    f.write(strings)

print(f'Done. Open {file_path} and copy results.')
