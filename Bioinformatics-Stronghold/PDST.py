# Problem 41: Creating a Distance Matrix.
# Uses two file paths. Adjust as necessary.

# Given a collection of DNA strings of equal length in FASTA format.
# Return the matrix corresponding to the p-distance on the given strings.
# Allowed an absolute error of 0.001.

# 1. Define a function to get hamming distance.
def get_hamming_distance(s1, s2):
    distance = 0
    for a, b in zip(s1, s2):
        if a != b:
            distance += 1
    return distance

# 2. Define a function to get the p-distance matrix from the given strings.
def get_distance_matrix(strings: list):
    n = len(strings)
    string_length = len(strings[0])
    matrix = [[0.0] * n for _ in strings]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = get_hamming_distance(strings[i], strings[j]) / string_length

    matrix = '\n'.join(' '.join(f'{value:.5f}' for value in row) for row in matrix)
    
    return matrix

# 3. Parse FASTA file for strings.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_pdst.txt'
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

# 4. Execute and write results in a separate file to preserve matrix format.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_pdst_output.txt'
with open(file_path, 'w') as f:
    f.write(get_distance_matrix(sequences))
