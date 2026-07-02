# Problem 23: Enumerating k-mers Lexicographically.
# Uses one file path. Adjust as necessary.
import itertools

# 1. Function to find all string permutations of a given length from a given alphabet.
def get_strings_from_alphabet(alphabet: list, length: int) -> str:
    kmers = itertools.product(alphabet, repeat=length)
    
    # Join each tuple into a string
    strings = [''.join(kmer) for kmer in kmers]

    return '\n'.join(strings)

# 2. Parse given file for ordered alphabet and string length.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_lexf.txt'
with open(file_path, 'r') as f:
    # .strip() removes the newline before splitting by spaces
    alphabet = f.readline().strip().split(' ')
    n = int(f.readline().strip())

# 3. Execute and print results.
print(get_strings_from_alphabet(alphabet, n))
