# Problem 51: Introduction to Set Operations.
# Uses two file paths. Adjust as necessary.

# Given a positive integer n and 2 subsets A and B of a larger set {1, 2, ..., n}.
# Return 6 sets, A union B, A intersection B, A - B, B - A, Ac, and Bc.

# 1. Define a function to output all six desired sets from n, A, and B.
def get_sets(n: int, A: set, B: set):
    # Get the first 4 sets using built-in set operations.
    union = A.union(B)
    intersection = A.intersection(B)
    ab_diff = A.difference(B)
    ba_diff = B.difference(A)
    # Get complements by iterating through set {1,2,...,n}, skipping elements in A & B.
    a_complement = set(i for i in range(1, n + 1) if i not in A)
    b_complement = set(j for j in range(1, n + 1) if j not in B)

    return f'{union}\n{intersection}\n{ab_diff}\n{ba_diff}\n{a_complement}\n{b_complement}'

# 2. Parse given file for n, A, and B. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_seto.txt'
with open(file_path, 'r') as f:
    n, A, B = [line.strip() for line in f if line.strip()]

n = int(n)
A = set(map(int, A.strip('{}').split(', ')))
B = set(map(int, B.strip('{}').split(', ')))

# 3. Execute and write results in an output file due to output size. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_seto_output.txt'
with open(file_path, 'w') as f:
    f.write(get_sets(n, A, B))

print(f'Executed! Copy results from {file_path}')
