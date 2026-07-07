# Problem 44: Edit Distance.
# Uses one file path. Adjust as necessary.

# Given two protein strings s and t in FASTA format.
# Return the edit distance dE(s, t).

# Edit distance of x,y is defined as the minimum number of edit operations needed to transform x into y.

# 1. Define a function to get the minimum cost edit distance from protein 1 to protein 2.
def get_edit_distance(p1: str, p2: str):
    m = len(p1)
    n = len(p2)
    
    # a. Initialize D with dimensions (m + 1) x (n + 1) to include case where len(p1) or len(p2) = 0.
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # b. Fill in base cases.
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j
    
    # c. For each cell, look at three previous choices. Start loop after base case (start at 1).
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            deletion = D[i - 1][j] + 1
            insertion = D[i][j - 1] + 1
            substitution = D[i - 1][j - 1]
            
            # Index string by -1 so as to exclude 0-length base case.
            if p1[i - 1] != p2[j - 1]:
                substitution += 1
            
            D[i][j] = min(deletion, insertion, substitution)
    
    # d. The lowest-cost edit distance is found at bottom-right corner.
    return D[m][n]

# 2. Parse given FASTA file for protein strings s and t. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_edit.txt'
with open(file_path, 'r') as f:
    sequences = []
    current_sequence = []
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith('>'):
            if current_sequence:
                sequences.append(''.join(current_sequence))
                current_sequence.clear()
        else:
            current_sequence.append(line)
    
sequences.append(''.join(current_sequence))
s, t = sequences

# 3. Execute and print results.
print(get_edit_distance(s, t))
