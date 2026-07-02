# Problem 36: k-Mer Composition.
# Uses two file paths. Adjust as necessary.

# The k-mer composition of a string encodes the number of times
# that each possible k-mer appears in the string.

# Given a DNA string s in FASTA format of length at most 100 kbp.
# Return the 4-mer composition of s.

import itertools

# 1. Define a function to get the k-mer composition of s.
def get_kmer_comp(string: str, kmer_length: int):
    # a. Get all possible DNA kmers of length kmer_length.
    kmers = itertools.product(['A', 'C', 'G', 'T'], repeat=kmer_length)
    kmer_counts = {''.join(kmer): 0 for kmer in kmers}

    # b. Slide a window of length kmer_length across the string once.
    # A string of length n can be composed of n - k + 1 overlapping k-mers.
    for i in range(len(string) - kmer_length + 1):
        window = string[i:i + kmer_length]
        if window in kmer_counts:
            kmer_counts[window] += 1
    
    # c. Return array A in proper format.
    return ' '.join(str(count) for count in kmer_counts.values())

# 2. Parse given file for string s.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_kmer.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    s = ''.join([line.strip().replace('\r', '').replace('\n', '').upper() for line in lines[1:]])

# Set k-mer length. This problem asks for all 4-mers.
kmer_length = 4

# 3. Execute and print results. Rosalind takes issue with terminal-printed version.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_kmer_output.txt'
with open(file_path, 'w') as f:
    f.write(get_kmer_comp(s, kmer_length))

print(f'Done. Open {file_path} and copy contents.')
