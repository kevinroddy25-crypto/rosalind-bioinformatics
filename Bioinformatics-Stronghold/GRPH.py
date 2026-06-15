# Problem 12: Overlap Graphs.

# Distill given file into dictionary of fasta IDs and corresponding strings.
file_path = 'path/to/your/rosalind_grph.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

fasta_dict = {}
current_id = ""

for line in lines:
    line = line.strip()
    if not line:
        continue  # Skip empty lines
    
    if line.startswith('>'):
        # Remove the '>' and use the ID as a dictionary key
        current_id = line[1:]
        fasta_dict[current_id] = []
    else:
        # Append the sequence fragment to the current ID
        fasta_dict[current_id].append(line)

# Join the lists of sequence fragments into single strings
for label in fasta_dict:
    fasta_dict[label] = "".join(fasta_dict[label])

# Iterate using .items() to keep track of both the FASTA ID (key) and the sequence (value)
f = open('Rosalind Info/Bioinformatics Stronghold/problem_12_output.txt', 'w')

for id1, seq1 in fasta_dict.items():
    for id2, seq2 in fasta_dict.items():
        
        # Ignore self-overlap.
        if id1 == id2:
            continue

        # Check if the prefix of seq1 matches the suffix of seq2.
        if seq1[:3] == seq2[-3:]:
            f.write(f"{id2} {id1}\n")

f.close()
