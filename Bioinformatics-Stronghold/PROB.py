# Problem 28: Introduction to Random Strings.
# Uses one file path. Adjust as necessary.

# Given DNA string s and array A.
# Return array B of equal length to array A in which B[k] represents log P(s has GC-content A[k]).

import math

# 1. Define a function to get list B wherein B[k] = log P(random string s w/ gc-content A[k] == s).
def get_random_string_prob(s: str, A: list) -> str:
    B = []
    
    probs = []
    for i in range(len(A)):
        gc_content = float(A[i])

        probs_of_bases = {'A': (1 - gc_content) / 2,
                          'T': (1 - gc_content) / 2,
                          'C': gc_content / 2,
                          'G': gc_content / 2
                          }
        
        probs = [probs_of_bases[base] for base in s]
        
        final_prob = 1
        for prob in probs:
            final_prob *= prob
        
        # Rosalind wants B to have common log of probabilities.
        # Rounded to the thousandth.
        final_prob = round(math.log10(final_prob), 3)
        
        B.append(str(final_prob))
    
    return ' '.join(B)
        
# 2. Parse the given file for string s and array A. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_prob.txt'
with open(file_path, 'r')  as f:
    s = f.readline().strip()
    A = f.readline().strip().split(' ')

# 3 Execute and print results.
print(get_random_string_prob(s, A))
