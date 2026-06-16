# Problem 16: Finding a protein motif.
# Uses two file paths.


# Import regex to find patterns.
import re

# 0. Retrieve the data...

# Input protein IDs into UniProt ID mapping tool: https://www.uniprot.org/help/id_mapping.
# Alternatively, load from text file, rosalind_mprt.txt.
# Download fasta file of canonical proteins and respective IDS (fasta_file_path), NOT COMPRESSED.

# 1. Create fasta_dict dictionary of protein IDs and acid sequences using UniProt fasta file. Adjust file path as necessary.
fasta_file_path = 'path/to/your/idmapping_0000_00_00.fasta'

with open(fasta_file_path, 'r') as f:
    lines = f.readlines()

fasta_dict = {}
current_id = None

for line in lines:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    if line.startswith('>'): # Set fasta_dict keys to IDs, filter between vertical bar separators.
        current_id = line[(line.find('|') + 1):(line.find('|', line.find('|') + 1))]
        fasta_dict[current_id] = []
    else: # Set fasta_dict values for current protein ID to lines of amino acid sequences that follow.
        fasta_dict[current_id].append(line)

# Conjoin respective values of all protein IDs to unify amino acid sequences.
for value in fasta_dict:
    fasta_dict[value] = ''.join(fasta_dict[value])

# 2. Update fasta_dict to ensure the ID name matches Rosalind's preferred format. Adjust file path as necessary.
problem_file_path = 'path/to/your/rosalind_mprt.txt'

with open(problem_file_path) as f:
    # Use strip() to remove newline characters (\n) from the file IDs
    rosalind_ids = [line.strip() for line in f if line.strip()]

# Create a new dictionary to hold the updated mappings
updated_fasta_dict = {}

for ros_id in rosalind_ids:
    for prot_id, prot_seq in fasta_dict.items():
        if prot_id in ros_id:
            # Map the clean Rosalind ID to the sequence
            updated_fasta_dict[ros_id] = prot_seq
            break  # Found the match, move to the next Rosalind ID

# 3. Replace the old dictionary with the new one
fasta_dict = updated_fasta_dict

# 4. Find the motif within each acid sequence in (updated) fasta_dict.

# By wrapping the pattern inside (?= ... ), the regex engine "looks ahead" to find the match, 
# but matches an empty string at the starting position. 
# This allows finditer to check every single starting index without skipping ahead.
motif_pattern = re.compile(r'(?=(N[^P][ST][^P]))')

motif_locations = {}

for prot_id, prot_seq in fasta_dict.items():
    # Because the lookahead matches an empty string, match.start() gives 
    # us the exact starting index of the motif. Rosalind uses 1-based indexing, however.
    matches = [str(match.start() + 1) for match in motif_pattern.finditer(prot_seq)]

    if matches:
        motif_locations[prot_id] = matches

# Print results.
for prot_id, locations in motif_locations.items():
    print(prot_id)
    print(' '.join(locations))
