# Problem 1: Count nucleotides in a given DNA string.

dna_string = input("Enter a DNA string: ")

num_A = dna_string.count('A')
num_C = dna_string.count('C')
num_G = dna_string.count('G')
num_T = dna_string.count('T')

print(num_A, num_C, num_G, num_T)
