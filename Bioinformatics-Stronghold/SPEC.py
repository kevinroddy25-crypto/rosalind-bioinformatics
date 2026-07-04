# Problem 46: Inferring Protein from Spectrum.
# Uses one file path. Adjust as necessary.

# Given a list L of n positive real numbers.
# Return a protein string of length n - 1 whose prefix spectrum
# is equal to L. Consult the monoisotopic mass table.

# This program ignores all potential instances of leucine (since isoleucine is its isomer, equal in mass).

# 1. Define a function to construct a protein string from prefix spectrum L.
def get_protein_from_prefix_spectrum(spectrum: list):

    # a. Rounded monoisotopic mass table.
    monoisotopic_masses = {
        'A': 71.04,
        'C': 103.01,
        'D': 115.03,
        'E': 129.04,
        'F': 147.07,
        'G': 57.02,
        'H': 137.06,
        'I': 113.08,
        'K': 128.09,
        'L': 113.08,
        'M': 131.04,
        'N': 114.04,
        'P': 97.05,
        'Q': 128.06,
        'R': 156.10,
        'S': 87.03,
        'T': 101.05,
        'V': 99.07,
        'W': 186.08,
        'Y': 163.06,
    }

    # b. Iterate through prefix spectrum to get each b-ion mass.
    ion_masses = []
    for i in range(len(spectrum) - 1):
        ion_masses.append(round((spectrum[i + 1] - spectrum[i]), 2))

    # c. Switch b-ion masses for corresponding acids.
    acids = []
    for ion_mass in ion_masses:
        for acid, mass in monoisotopic_masses.items():
            if ion_mass == mass:
                acids.append(acid)
                break
    
    return ''.join(acids)

# 2. Parse given file for L. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_spec.txt'
with open(file_path, 'r') as f:
    L = [float(line.strip()) for line in f.readlines() if line]

# 3. Execute and print results.
print(get_protein_from_prefix_spectrum(L))
