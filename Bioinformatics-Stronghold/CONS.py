# Problem 10: Consensus and profile matrix.

# Given a collection of at most 10 DNA strings of equal length in f FASTA.
# Return a consensus string and profile matrix for the collection.

# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_cons.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

strings = []
current_seq = []

# Compile only nb sequences in list strings.
for line in lines:
    line = line.strip()

    if line.startswith('>'):
        # If we already have sequence data accumulated, glue it together and save it
        if current_seq:
            strings.append("".join(current_seq))
            current_seq = []  # Reset the accumulator for the next sequence
    else:
        # If it's a sequence line, add it to our accumulator
        current_seq.append(line)

# Append the very last sequence once loop finishes.
if current_seq:
    strings.append(''.join(current_seq))

# Create profile matrix based on strings.

# Find the length of the strings.
string_len = len(strings[0])

# Initialize the profile matrix with zeroes.
profile_matrix = {
    'A': [0] * string_len,
    'C': [0] * string_len,
    'G': [0] * string_len,
    'T': [0] * string_len
}

# Loop through each string and increment count at position.
for string in strings:
    for i in range(len(string)):
        nucleotide = string[i]

        if nucleotide in profile_matrix:
            profile_matrix[nucleotide][i] += 1

# Find the consensus.
consensus = []

for i in range(string_len):
    max_count = -1
    best_base = ''

    # Check which nucleotide has the highest count @ position i.
    for base in ['A', 'C', 'G', 'T']:
        if profile_matrix[base][i] > max_count:
            max_count = profile_matrix[base][i]
            best_base = base
    
    consensus.append(best_base)

# Print the consensus and profile matrix in a separate file. Adjust file path as necessary.
with open('path/to/your/rosalind_cons_output.txt', 'w') as f:
    # Write consensus.
    f.write(''.join(consensus) + '\n')

    # Write profile matrix in desired format.
    for base, counts in profile_matrix.items():
        counts_formatted = ' '.join(str(num) for num in counts)

        f.write(f'{base}: {counts_formatted} \n')
