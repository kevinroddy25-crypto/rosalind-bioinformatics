# Problem 14: Finding a shared motif.

# Distill given file into dictionary (fasta_dict) of fasta ID keys and corresponding string values.
# Adjust file path as necessary.

file_path = 'path/to/your/rosalind_lcsm.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

fasta_dict = {}
current_id = None

for line in lines:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    if line.startswith('>'):
        current_id = line[1:]
        fasta_dict[current_id] = []
    else:
        fasta_dict[current_id].append(line)

# Join the lists of sequence fragments into single strings
for label in fasta_dict:
    fasta_dict[label] = ''.join(fasta_dict[label])

# Find the shortest sequence by length.
shortest_seq = min(fasta_dict.values(), key=len)

# Check whether a candidate substring is present in all sequences.
def is_shared_motif(subseq):
    return all(subseq in seq for seq in fasta_dict.values())

# Check progressively smaller sliding windows of the shortest seq.
# Break when a match is found in all sequences.
longest_shared_motif = ''
shortest_len = len(shortest_seq)

for length in range(shortest_len, 0, -1):

    for start in range(shortest_len - length + 1):
        candidate = shortest_seq[start: start + length]

        if is_shared_motif(candidate):
            longest_shared_motif = candidate
            break

    if longest_shared_motif:
        break

# Keep in mind there are often multiple longest shared motifs.
# Especially when the strings in the database become less alike.

# Output longest shared motif in a new file. Adjust as necessary.
with open('path/to/your/rosalind_lcsm_output.txt', 'w') as f:
    f.write(longest_shared_motif)
