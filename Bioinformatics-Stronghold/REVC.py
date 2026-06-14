# Problem 3: Generate the reverse complement of a string of DNA (s).

s = input('Enter a DNA string: ')

complementary_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

c = []

for letter in s:
    letter = complementary_bases[letter]
    c.append(letter)

c.reverse()

print('The reverse complement is:', ''.join(c))
