# Problem 40: Maximum Matchings and RNA Secondary Structures.
# Uses one file path. Adjust as necessary.

# Given an RNA string s.
# Return the total number of possible maximum machings of basepair edges in the bonding graph of s.

from math import perm

# 1. Define a function to determine the maximum number of matchings.
def get_num_max_matchings(rna: str):
    # Because AU and CG pair independently, max matchings = AU combinations * CG combinations.
    counts = {base: rna.count(base) for base in ['A', 'C', 'G', 'U']}
    max_AU, min_AU = max(counts['A'], counts['U']), min(counts['A'], counts['U'])
    max_CG, min_CG = max(counts['C'], counts['G']), min(counts['C'], counts['G'])

    return perm(max_AU, min_AU) * perm(max_CG, min_CG)

# 2. Parse given file for RNA string s.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_mmch.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

s = ''.join([line.strip() for line in lines[1:]])

# 3. Execute and print results.
print(get_num_max_matchings(s))
