# Problem 9: Finding a motif in DNA.

# Given two DNA strings s and t. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_subs.txt'

with open(file_path, 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

def get_motif_locations(s, t):
    # Return all locations of t as a substring of s.
    motif_locations = []

    # Start searching at beginning of strand s.
    position = s.find(t)

    while position != -1:
        # Rosalind requires 1-based indexing.
        motif_locations.append(str(position + 1))

        # Move forward by 1 to check for overlapping matches.
        position = s.find(t, position + 1)
    
    return motif_locations

motif_locations = ' '.join(get_motif_locations(s, t))
print(motif_locations)
