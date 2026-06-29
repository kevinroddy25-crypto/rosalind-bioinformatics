# Problem 32: Completing a Tree.
# Uses one file path. Adjust as necessary.

# Models the construction of a phylogeny.

# Given a positive integer n, representing the number of nodes on a given graph that contains no cycles,
# and a corresponding adjacency list.
# Return the minimum number of edges that can be added to the graph to produce a tree.

# 1. Define a function to get the minimum number of edges to construct a tree.
def get_min_edges(n: int, num_edges: int):
    
    # Edges to add = nodes - (existing edges + 1)
    min_edges = n - num_edges - 1
    return min_edges

# 2. Parse file for n and adjacencies. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_tree.txt'
with open(file_path, 'r') as f:
    n = int(f.readline().strip())
    
    num_edges = len([line for line in f.readlines() if line.strip()])

# 3. Execute and print results.
print(get_min_edges(n, num_edges))
