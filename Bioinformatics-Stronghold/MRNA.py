# Problem 17: Inferring mRNA from protein.
# One file path, adjust as necessary.

# Objective: return the total number of different RNA strings
# that code for a given protein string, modulo 10^6.

# Given prot = MA
# Output = 12

# Dictionary of acids and corresponding mRNA codons.
acid_to_codons = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'Y': ['UAU', 'UAC'],
    'Stop': ['UAA', 'UAG', 'UGA'],
    'C': ['UGU', 'UGC'],
    'W': ['UGG'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG']
}

# Function to get number of configurations of RNA that code for protein.
def get_num_rna_configurations(protein):
    num_configurations = 1

    for acid in prot:
        num_configurations *= len(acid_to_codons[acid])
    
    # 3 codons ('UAA', 'UAG', 'UGA') all code for stop @ end of the sequence.
    num_configurations *= 3

    return num_configurations

# Get protein from Rosalind file. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_mrna.txt'
with open(file_path, 'r') as f:
    prot = f.readline().strip()

# Return permutations modulo 10^6.
print(get_num_rna_configurations(prot) % 1000000)
