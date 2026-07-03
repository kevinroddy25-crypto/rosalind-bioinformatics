# Problem 38: Finding a Shared Spliced Motif.
# Uses one file path. Adjust as necessary.

# Given two DNA strings s and t in FASTA format.
# Return a longest common subsequence of s and t.

# 1. Define a function to get the longest common subsequence in two strings.
def get_longest_common_subsequence(s: str, t: str):
    # a. Initialize matrix L.
    L = [[0] * (len(t) + 1) for row in range(len(s) + 1)]

    # b. Fill in matrix L using DP.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    # c. Reconstruct the longest common subsequence.
    i = len(s)
    j = len(t)
    u = []
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            u.append(s[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # d. Return u, the longest common subsequence, in the correct order.
    return ''.join(reversed(u))

# 2. Parse given file for strings s and t. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_lcsq.txt'
with open(file_path, 'r') as f:
    strings = {}
    current_string = 0
    for line in f.readlines():
        line = line.strip().replace('\r', '').replace('\n', '')
        if not line:
            break
        
        if line.startswith('>'):
            current_string += 1
            strings[current_string] = ''
        else:
            strings[current_string] += line
    
s = ''.join(strings[1])
t = ''.join(strings[2])

# 3. Execute and print results.
print(get_longest_common_subsequence(s, t))
