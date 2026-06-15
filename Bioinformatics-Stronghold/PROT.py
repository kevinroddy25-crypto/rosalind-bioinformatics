# Problem 8: Translating RNA into its corresponding protein / amino acid.

# Dictionary of codon keys corresponding to amino acid values.
codon_to_acid = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# 1. Read the mRNA string directly. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_prot.txt'

with open(file_path, 'r') as f:
    s = f.readline().strip()

# 2. Function to convert mRNA string into a list of string codons
def convert_mrna_to_codons(mrna_str):
    # Slicing the string directly gives us 3-character STRINGS (e.g., "AUG")
    codons = [mrna_str[i:i+3] for i in range(0, len(mrna_str), 3)]
    return codons

# 3. Function to return the protein string, halting at the Stop codon
def get_protein_from_codon(codons):
    proteins = []

    for codon in codons:
        acid = codon_to_acid[codon]
        if acid == "Stop":  # Break when you hit the stop codon per Rosalind rules
            break
        proteins.append(acid)

    return ''.join(proteins)

# 4. Return the protein string encoded by s.
codons = convert_mrna_to_codons(s)
proteins = get_protein_from_codon(codons)

# Because the output will be long, create a new file to house output. Adjust file path as necessary.
with open('path/to/your/rosalind_prot_output.txt', 'w') as f:
    f.write('The encoded protein string is: \n')
    f.write(proteins)
