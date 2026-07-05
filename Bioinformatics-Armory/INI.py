# Problem 1: Introduction to the Bioinformatics Armory.
# Identical to Bioinformatics Stronghold problem: Counting DNA Nuleotides.

# Given a DNA string s.
# Return four integers separated by spaces representing the respective number of times
# the symbols ACTG occur in s.

# Simply learning the sequence data type in BioPython.

from Bio.Seq import Seq
s = Seq(''.join(input('Enter a string s: ').splitlines()))
print(' '.join([str(s.count(base)) for base in ['A', 'C', 'G', 'T']]))
