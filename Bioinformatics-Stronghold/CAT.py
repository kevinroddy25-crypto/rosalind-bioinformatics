# Problem 33: Catalan Numbers and RNA Secondary Structures.
# Uses one file path. Adjust as necessary.

# Given an RNA string s wherein A and U occur equally and C and G occur equally.
# Return the total number of noncrossing perfect matchings of basepair edges in the bonding graph of s % 10^6.

# 1. Define a function to count RNA matchings % 10^6 via memoization.
def count_rna_matchings(s, memo={}):
    # An empty string has 1 valid matching.
    if not s:
        return 1
    
    # Return stored result if already calculated.
    if s in memo:
        return memo[s]
    
    total_matchings = 0
    # base 0 must pair with some base k.
    # k must be odd so that split intervals s[1:k] and s[k+1:] have even lengths.
    for k in range(1, len(s), 2):
        if (s[0], s[k]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
            left_sub = s[1:k]
            right_sub = s[k+1:]
        
            # Only recurse if the substrings have balanced base counts.
            if (left_sub.count('A') == left_sub.count('U') and
                left_sub.count('C') == left_sub.count('G')):
                
                total_matchings += count_rna_matchings(left_sub, memo) * count_rna_matchings(right_sub, memo)

    # Store the result % 10^6.
    memo[s] = total_matchings % 1000000
    return memo[s]

# 2. Parse given file for RNA string s. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_cat.txt'
with open(file_path, 'r') as f:
    s = ''.join([line.strip() for line in f.readlines() if line and not line.startswith('>')])

# 3. Execute and print results.
print(count_rna_matchings(s))
