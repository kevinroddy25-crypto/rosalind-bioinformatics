# Problem 37: Speeding Up Motif Finding.
# Uses two file paths. Adjust as necessary.

# Given a DNA string s in FASTA format.
# Return the failure array of s.

# The failure array of s is an array P of a length equivalent to the length of s.
# P[k] is the length of the longest substring s[j:k], equal to some prefix s[1:k-j+1]

# 1. Define a function to get the failure array of s.
def get_failure_array(s):
    failure = [0] * len(s)
    j = 0 # j tracks len(current longest prefix/suffix match).
    for k in range(1, len(s)):
        while j > 0 and s[k] != s[j]:
            j = failure[j - 1]
        if s[k] == s[j]:
            j += 1
        failure[k] = j

    return ' '.join(map(str, failure))

# 2. Parse the given file for string s. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_kmp.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

s = ''.join([line.strip().replace('\r', '').replace('\n', '').upper() for line in lines[1:]])

# 3. Execute and print results. Since the string is LONG, write in an output file.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_kmp_output.txt'
with open(file_path, 'w') as f:
    f.write(get_failure_array(s))

print(f'Done. Open {file_path} and copy contents.')
