# Problem 22: RNA Splicing.
# Uses one file path. Adjust as necessary.

# Given a DNA string and a collection of substrings acting as introns in FASTA format.
# Return a protein string resulting from transcribing and translating the exons of s.

# 1. Function to remove all intron instances and "splice" the exons together.
def splice(string: str, introns: list) -> str:
    for intron in introns:
        string = string.replace(intron, '')
    
    return string

# 2. Function to convert exon-only string into a protein string.
def get_protein_from_dna(string: str) -> str:
    dna_codons = [string[i:i+3] for i in range(0, len(string), 3)]

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
    amino_acids = []
    for codon in dna_codons:
        if codon in dna_to_acid:
            acid = dna_to_acid[codon]
            if acid == 'Stop':
                break
            amino_acids.append(dna_to_acid[codon])
    
    
    return ''.join(amino_acids)

# 3. Parse FASTA file for DNA string and substrings (describing introns).
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_splc.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

fasta_sequences = []
current_seq = []

for line in lines:
    line = line.strip()
    if line.startswith('>'):
        if current_seq:
            fasta_sequences.append(''.join(current_seq))
            current_seq = []
    else:
        current_seq.append(line)
if current_seq:
    fasta_sequences.append(''.join(current_seq))

string = fasta_sequences[0]
introns = fasta_sequences[1:]

# 4. Execute and print results.
protein = get_protein_from_dna(splice(string, introns))
print(protein)
