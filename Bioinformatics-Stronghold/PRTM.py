# Problem 20: Calculating Protein Mass.

# The mass of a protein is the
# Sum of masses of all residues + one water molecule.
    ## A residue is a dehydrated amino acid post peptide bond formation.
    ## Weirdly, the solution did not want the additional mass of the water molecule ...

# 1. Create a dictionary containing the monoisotopic masses of each aa.
monoisotopic_masses = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

# 2. Function to get the weight of a given protein string.
def get_weight(protein: str):
    weight = 0.0

    for acid in protein:
        weight += monoisotopic_masses[acid]
    
    weight = round(weight, 3)
    return weight

# 3. Get protein string p from given file containing P of length at most 1000 aa.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_mprt.txt'
with open(file_path, 'r') as f:
    p = f.readline()

# 4. Print the weight of p.
weight = get_weight(p)
print(weight)
