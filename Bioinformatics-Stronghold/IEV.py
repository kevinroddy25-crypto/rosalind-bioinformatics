# Problem 13: Calculating Expected Offspring.
# Uses one file path. Adjust as necessary.

# Given: Six nonnegative integers, each of which does not exceed 20,000. 
# The integers correspond to the number of couples in a population possessing 
# each genotype pairing for a given factor. In order, the six given integers
# represent the number of couples having the following genotypes:
# AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

# Return the expected number of offspring displaying the dominant phenotype.
# Assuming each couple has exactly two offspring.

# 1. Define a function to determine E(dominant).
def get_expected_dominant_offspring(couples):
    
      probs = [1, 1, 1, 0.75, 0.5, 0]

      e = 0
      for i in range(6):
            if couples[i]:
                  e += 2 * int(couples[i]) * probs[i]

      return e

# 2. Parse file for couple data AA-AA through aa-aa. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_iev.txt'
with open(file_path, 'r') as f:
      couples = f.readline().split(' ')

# 3. Execute and print results.
print(get_expected_dominant_offspring(couples))
