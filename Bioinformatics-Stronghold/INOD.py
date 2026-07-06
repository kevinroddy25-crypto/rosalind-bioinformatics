# Problem 35: Counting Phylogenetic Ancestors.

# An unrooted binary tree is one in which all internal (non-leaf) nodes have degree 3.

# Given a positive integer n.
# Return the number of internal nodes of any unrooted binary trees having n leaves.

# 1. Define a function to get the number of internal nodes of an unrooted binary tree having n leaves.
def get_num_internal_nodes_from_leaves(n: int):
    return n - 2

# 2. Get n from input.
n = int(input('Enter a positive integer n: ').strip())

# 3. Execute and print results.
print(get_num_internal_nodes_from_leaves(n))
