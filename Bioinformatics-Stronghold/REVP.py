# Problem 21: Locating Restriction Sites.
# Uses one file path; adjust as necessary.

# Given a DNA string of length at most 1 kbp in FASTA format.
# Return the position and length of every reverse palindrome
# in the string having length between 4 and 12 bp.

# 1. Define a function to find restriction sites.
def find_restriction_sites(dna_string: str):
    base_complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    results = []
    n = len(dna_string)

    # Reverse palindromes must have an even length.
    # Therefore, the center is always between two indices: i and i + 1.
    for i in range(n - 1):
        left = i
        right = i + 1
        current_length = 0
        
        # Expand outwards from the center
        while left >= 0 and right < n:
            # Check if the outward bases are complements
            if base_complements[dna_string[left]] == dna_string[right]:
                current_length += 2
                
                # Check if this valid reverse palindrome falls within the 4-12 bp window
                if 4 <= current_length <= 12:
                    # Rosalind format demands: 1-based start position and the length
                    start_position = left + 1 
                    results.append((start_position, current_length))
                
                # If the maximum size of 12 is hit, stop expanding this center
                if current_length == 12:
                    break
                    
                left -= 1
                right += 1
            else:
                # The moment a complement match breaks, no larger palindrome can exist here
                break

    # Rosalind wants the output ordered by position, then length.
    results.sort(key=lambda x: (x[0], x[1]))
    return results

# 2. Parse the given FASTA file and store the string. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_revp.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

string_parts = []
for line in lines:
    if line.startswith('>'):
        continue
    string_parts.append(line.strip())

dna_sequence = ''.join(string_parts)

# 3. Execute and print results.
restriction_sites = find_restriction_sites(dna_sequence)

for pos, length in restriction_sites:
    print(f'{pos} {length}')
