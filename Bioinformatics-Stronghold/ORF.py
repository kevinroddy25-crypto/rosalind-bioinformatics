# Problem 18: Open Reading Frames.
# Read a FASTA file and print distinct protein strings from ORFs.

file_path = 'Rosalind Info/Bioinformatics Stronghold/rosalind_orf.txt'

fasta_dict = {}
current_id = None
with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            current_id = line[1:]
            fasta_dict[current_id] = []
        else:
            fasta_dict[current_id].append(line)

for label in fasta_dict:
    fasta_dict[label] = ''.join(fasta_dict[label])

# 2. Return: Every distinct candidate protein string that can be translated from ORFs of s
# Strings can be returned in any order.

dna_to_acid = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop",
    "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Transcribe DNA string s into corresponding acid sequence.
# Function to convert a DNA string into a list of codons.
def convert_dna_to_codons(dna_seq):
    return [dna_seq[i:i+3] for i in range(0, len(dna_seq) - 2, 3)]

# Function to convert DNA string into its antisense complement.
def reverse_complement(dna_seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna_seq))

# Function to translate DNA string from a given start index.
def translate_from_start(dna_seq, start_index):
    protein = []
    for i in range(start_index, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        acid = dna_to_acid.get(codon)
        if acid == 'Stop':
            return ''.join(protein)
        if acid is None:
            return None
        protein.append(acid)
    return None

# Function to find open reading frames.
def find_orfs(dna_seq):
    proteins = set()
    for frame in range(3):
        for i in range(frame, len(dna_seq) - 2, 3):
            if dna_seq[i:i+3] == 'ATG':
                protein = translate_from_start(dna_seq, i)
                if protein:
                    proteins.add(protein)
    return proteins

# Create set of proteins in each ORF and print iteratively.
proteins = set()
for dna_sequence in fasta_dict.values():
    proteins.update(find_orfs(dna_sequence))
    proteins.update(find_orfs(reverse_complement(dna_sequence)))

for protein in proteins:
    print(protein)
