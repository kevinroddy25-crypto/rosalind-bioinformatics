# Distill the given file into string codes and values. Adjust file path as needed.
file_path = 'path/to/your/rosalind_gc.txt'

with open(file_path, 'r') as f:
    lines = f.readlines()

fasta_dict = {}
current_id = ""

# This part is really clever. Keep in mind for synthesis of any fasta data.
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

# Find the ID with the HIGHEST GC content
highest_gc_id = None
highest_gc_content = -1.0

for label, sequence in fasta_dict.items():
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_nt = len(sequence)
    
    # Calculate GC percentage
    gc_content = (g_count + c_count) / total_nt * 100
    
    if gc_content > highest_gc_content:
        highest_gc_content = gc_content
        highest_gc_id = label

# Print results in Rosalind's expected format
print(highest_gc_id)
print(f"{highest_gc_content:.6f}")
