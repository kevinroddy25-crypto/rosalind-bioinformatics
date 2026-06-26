# Problem 25: Genome Assembly as Shortest Superstring.
# One file path. Adjust as necessary.
# Download networkx if necessary.

# Given at most 50 DNA strings of approx. = length in FASTA format,
# Which represent reads deriving from the same strand of a single linear chromosome.

# Return a shortest superstring containing all the given strings.

import networkx as nx

# Function to get overlap of two strings.
def get_overlap(string1, string2):
    # Start with the maximum possible overlap length
    max_possible = min(len(string1), len(string2))
    
    # Check prefixes and suffixes using slicing
    for i in range(max_possible, 0, -1):
        if string1.endswith(string2[:i]):
            return i  # Returns the length of the overlap
            
    return 0  # When no overlap found

# Use overlap graphs to find the most optimal path.
def get_shortest_superstring(strings: list) -> str:

    # 1. Create an overlap graph with strings as nodes.
    D = nx.DiGraph()

    D.add_nodes_from(strings)
    
    # 2. Calculate overlap between every pair of strings.
    edges_to_add = []

    for string1 in strings:
        for string2 in strings:
            
            if string1 == string2:
                continue

            overlap_len = get_overlap(string1, string2)
            
            # Draw a directed arrow between each pair of strings.
            if overlap_len > 0:
                edges_to_add.append((string1, string2, overlap_len))
            D.add_weighted_edges_from(edges_to_add)

    # 3. Find the heaviest edge, merge, update edges, and repeat.
    while D.number_of_nodes() > 1:
        # a. Find the heaviest edge.
        heaviest_edge = max(D.edges(data=True), key=lambda edge: edge[2]['weight'])

        node_a, node_b, edge_data = heaviest_edge
        overlap_len = edge_data['weight']

        # b. Merge the two strings.
        merged_string = node_a + node_b[overlap_len:]
        
        # c. Remove the old nodes from the graph.
        D.remove_node(node_a)
        D.remove_node(node_b)

        # d. Calculate the overlaps between the new merged string and remaining nodes.
        remaining_nodes = list(D.nodes)
        D.add_node(merged_string)
        
        for other_node in remaining_nodes:
            weight1 = get_overlap(merged_string, other_node)
            if weight1 > 0:
                D.add_edge(merged_string, other_node, weight=weight1)
            
            weight2 = get_overlap(other_node, merged_string)
            if weight2 > 0:
                D.add_edge(other_node, merged_string, weight=weight2)
            
    # 4. The last remaining node is the shortest common superstring.
    shortest_superstring = list(D.nodes())[0]
    
    return shortest_superstring

# Parse FASTA file. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_long.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

strings = []
current_seq = []

for line in lines:
    line = line.strip()
    if line.startswith('>'):
        # Start piecing together new string
        if current_seq:
            strings.append(''.join(current_seq))
            current_seq = []
    else:
        current_seq.append(line)

if current_seq:
    strings.append(''.join(current_seq))

print(get_shortest_superstring(strings))
