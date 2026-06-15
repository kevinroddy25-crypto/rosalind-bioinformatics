# Given: Two DNA strings s1 and s2 of equal length (not exceeding 1 kbp).
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_hamm.txt'

with open(file_path, 'r') as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

# Function to count the Hamming distance (measure of how many point mutations) between s1 and s2.
def get_hamming_distance(s1, s2):
    distance = 0
    for a, b in zip(s1, s2):
        if a != b:
            distance += 1
    return distance

# Output the Hamming distance between s1 and s2.
hamming_distance = get_hamming_distance(s1, s2)
print(str(hamming_distance))
