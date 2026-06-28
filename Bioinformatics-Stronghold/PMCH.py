# Problem 26: Perfect Matchings and RNA Secondary Structures.
# One file path. Adjust as necessary.

# Given an RNA string having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
# Return the total possible number of perfect matchings of basepair edges in the bonding graph of the string.

import math

# 1. Parse given FASTA file for string. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_pmch.txt'

string_parts = []
with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>') or not line:
            continue
        string_parts.append(line)

rna_string = ''.join(string_parts)

# 2. Count the occurrences of each nucleobase
count_A = rna_string.count('A')
count_C = rna_string.count('C')

# 3. Calculate total perfect matchings using factorials
# Total = (A!) * (C!):
# The total number of AU pairings with x 'A's and x 'U's is A!
# The fundamental counting principle states this for both AU and CG pairs.
# Because AU and CG pairs are independent, the product rule means (A!)(U!) = total perfect matchings.
total_perfect_matchings = math.factorial(count_A) * math.factorial(count_C)

# 4. Print results
print(total_perfect_matchings)
