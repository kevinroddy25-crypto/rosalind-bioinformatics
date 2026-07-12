# Problem 50: Interleaving Two Motifs.
# Uses one file path. Adjust as necessary.

# Given two DNA strings s and t.
# Return a shortest common supersequence of s and t.

# 1. Define a function to get the shortest common supersequence.
def get_scs(s: str, t: str):
    # a. Initialize grid D with m + 1 rows and n + 1 columns.
    n, m = len(s), len(t)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    # b. Fill out grid D wherein D[i][j] = the length of the SCS
    # of the substrings string prefixes s[0...i - 1] and t[0...j - 1].
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0: # Account for base case wherein len(s) = 0.
                D[i][j] = j
            elif j == 0: # Account for base case wherein len(t) = 0.
                D[i][j] = i
            elif s[i - 1] == t[j - 1]:
                D[i][j] = 1 + D[i - 1][j - 1]
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1])

    # c. Backtrack through grid D to get SCS.
    scs = []
    i, j = n, m
    while i > 0 or j > 0:
        # Handle boundaries. Append remaining string if one string has been appended fully.
        if i == 0:
            scs.append(t[j - 1])
            j -= 1
        elif j == 0:
            scs.append(s[i - 1])
            i -= 1
        # If the base matches for s and t, append and move diagonally.
        elif s[i - 1] == t[j - 1]:
            scs.append(s[i - 1])
            i -= 1
            j -= 1
        # If the bases mismatch, append base of s or t that leads to shorter SCS.
        elif D[i - 1][j] < D[i][j - 1]:
            scs.append(s[i - 1])
            i -= 1
        else:
            scs.append(t[j - 1])
            j -= 1

    # d. Return SCS.
    return ''.join(reversed(scs))
 
# 2. Parse given file for strings s and t. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_scsp.txt'
with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

# 3. Execute and print results, ensuring no errors from line reading.
if len(lines) >= 2:
    s, t = lines[0], lines[1]
    print(get_scs(s, t))
