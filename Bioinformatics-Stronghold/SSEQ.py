# Problem 30: Finding a Spliced Motif.
# One file path. Adjust as necessary.

# Given two DNA strings s and t in FASTA format.
# Return one collection of indices of s where the symbols of t appear as a subsequence of s.

# 1. Define a function to get the indices of occurrence of t as a subsequence in s.
def get_subseq_location(s: str, t: str):
    # Find indices where t found as a subseq of s (1-based).
    indices = []
    n = 0
    for i, base in enumerate(s):
        if n < len(t) and base == t[n]:
            indices.append(i + 1)
            n += 1
            if n == len(t):
                break
    return indices

# 2. Parse FASTA file for s and t.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_sseq.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

s = []
t = []
n = 0
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('>'):
        n += 1
    elif n == 1:
        s.append(line)
    elif n == 2:
        t.append(line)

s = ''.join(s)
t = ''.join(t)

# 3. Execute and print results.
print(' '.join(map(str, get_subseq_location(s, t))))
