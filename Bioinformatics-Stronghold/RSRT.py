# Problem 42: Matching Random Motifs.
# Uses one file path. Adjust as necessary.

# Given a positive integer N, a number x between 0 and 1, and a DNA string s.
# Return the probability that if N random DNA strings that have the same length as s
# and are constructed with GC-content x, then at least one of the strings will equal s.

# 1. Define a function to get the probability that at least one string equals s.
def get_prob_rand_string_equals_string(n: int | float, x: float, string: str) -> float:
    # a. Calculate and store the probability that a random string 
    # with equal gc-content to the given string is equivalent to the given string.
    gc_content = x
    
    probs_of_bases = {
                        'A': (1 - gc_content) / 2,
                        'T': (1 - gc_content) / 2,
                        'C': gc_content / 2,
                        'G': gc_content / 2
                     }
        
    probs = [probs_of_bases[base] for base in string]
        
    p = 1
    for prob in probs:
        p *= prob
    
    # b. Using the complement rule, P(at least one success) = 1 - (1 - p)^n,
    # get the probability that at least one of n random strings = the given string.
    total_prob = 1 - (1 - p) ** n
    
    return round(total_prob, 3)

# 2. Parse given file for n, x, and string. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_rsrt.txt'
with open(file_path, 'r') as f:
    n, x = map(float, f.readline().strip().split(' '))
    string = f.readline().strip()

# 3. Execute and print results.
print(get_prob_rand_string_equals_string(n, x, string))
