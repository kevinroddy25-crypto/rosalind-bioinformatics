# Problem 58: Inferring Peptide from Full Spectrum.
# Uses one file path. Adjust as necessary.

# Given A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P,
# and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that
# if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

# Return A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p
# and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string 
# whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.

# 1. Define a function to infer peptide from parent mass and b/y ions.
def infer_peptide_from_parent_mass(parent_mass: float, ion_list: list[float]):
    monoisotopic_masses = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333,
    }

    # Sort the spectrum.
    sorted_ions = sorted([mass for mass in ion_list])
    
    # Calculate target length of the protein string n
    n = len(sorted_ions) // 2 - 1
    
    peptide = []
    current_mass = sorted_ions[0]
    
    # Traverse the sorted ions to find matching amino acid differences
    while len(peptide) < n:
        found_next = False
        for next_mass in sorted_ions:
            diff = next_mass - current_mass
            
            # Check if this difference matches any amino acid mass (within 0.01 tolerance)
            for residue, mass in monoisotopic_masses.items():
                # Absolute tolerance of 0.01
                if abs(diff - mass) < 0.01:
                    peptide.append(residue)
                    current_mass = next_mass
                    found_next = True
                    break
            if found_next:
                break
        
        # If we get stuck, it means we hit a dead end or mixed a b/y ion step
        if not found_next:
            return "Failed to infer."

    return ''.join(peptide)

# 2. Parse given file for parent mass and ions. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_full.txt'
with open(file_path, 'r') as f:
    lines = list(map(float, [line.strip() for line in f]))

parent_mass = lines[0]
ion_list = lines[1:]

# 3. Execute and print results.
print(infer_peptide_from_parent_mass(parent_mass, ion_list))
