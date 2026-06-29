# Problem 31: Transitions and Transversions.
# Uses one file path. Adjust as necessary.

# The transition/transversion is a useful calculation b/c 
# the ratio of sections of coding DNA tends to exceed the genomic average of 2.

# Given two DNA strings s1 and s2.
# Return the transition/transversion ratio R(s1, s2).

# A transition is a point mutation between purines (A, G) or between pyrimidines (T, C).
# A transversion is a point mutation between a purine and a pyrimidine.

# R(s1, s2) = num_transitions / num_transversions.

# 1. Define a function to check if mutation a -> b is a transition.
def is_transition(a, b):
    transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    if b == transitions[a]:
        return True
    
    return False

# 2. Define a function to find R(s1, s2).
def get_ratio(s1, s2):

    transitions = 0
    transversions = 0
    for a, b in zip(s1, s2):
        if a != b:
            if is_transition(a, b):
                transitions += 1
            else:
                transversions += 1
    
    return round(transitions / transversions, 11)

# 3. Parse given file for strings s1 and s2. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_tran.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

s1 = []
s2 = []
current_string = 0
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('>'):
        current_string += 1
    elif current_string == 1:
        s1.append(line)
    elif current_string == 2:
        s2.append(line)

s1 = ''.join(s1)
s2 = ''.join(s2)

# 4. Execute and print results.
print(get_ratio(s1, s2))
