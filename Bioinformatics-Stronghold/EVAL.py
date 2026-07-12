# Problem 47: Expected Number of Restriction Sites.
# Uses one file path. Adjust as necessary.

# Given a positive integer n, a DNA string s of even 
# length at most 10, and an array A of at most 20 numbers between 0 and 1.

# Return an array B having the same length as A in which B[i] is the expected
# number of times that s will appear as a substring of a random DNA string t of
# length n, where t is formed with gc-content A[i].

# 1. Define a function to get array B from the data.
def get_probability_array(n: int, string: str, gc_contents: list):
    # a. Linearity of Expectation:
    # Count slots (starting positions) of string in a random string of length n.
    slots = n - len(string) + 1

    # Get the number of G/C nucleotides and A/T nucleotides.
    n_gc = string.count('G') + string.count('C')
    n_at = string.count('A') + string.count('T')

    # b. Fill B by iterating through gc contents in A.
    B = []
    for gc_content in gc_contents:
        prob = (gc_content / 2) ** n_gc * ((1 - gc_content) / 2) ** n_at

        expected_matches = slots * prob
        B.append(f'{expected_matches:.3f}')

    # c. Return B.
    return ' '.join(B)

# 2. Parse file for n, s, and A. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_eval.txt'
with open(file_path, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

n, s = int(lines[0]), lines[1]
A = [float(element) for element in lines[2].split(' ')]

# 3. Execute and print results.
print(get_probability_array(n, s, A))
