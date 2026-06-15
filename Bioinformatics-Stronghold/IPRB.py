# Problem 7: Mendel's First Law
# Given integers k, m, and n, representing population containing k+m+n organism.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_iprb.txt'

with open(file_path, 'r') as f:
    k, m, n = map(int, f.readline().split())

# k = number of XX individuals
# m = number of Xx individuals
# n = number of xx individuals

# Return the probability that two randomly selected mating organisms
# will produce an individual possessing X_ (dominant phenotype).
# Assume any two organisms can mate.

print(k, m, n)

def get_prob_dominant(k, m, n):
    total = k + m + n
    prob_dominant = 0

    # XX and XX
    prob_dominant += (k / total) * ((k - 1) / (total - 1))

    # XX and Xx
    prob_dominant += (k / total) * (m / (total - 1)) * 1
    prob_dominant += (m / total) * (k / (total - 1)) * 1

    # XX and xx
    prob_dominant += (k / total) * (n / (total - 1)) * 1
    prob_dominant += (n / total) * (k / (total - 1)) * 1

    # Xx and Xx
    prob_dominant += (m / total) * ((m - 1) / (total - 1)) * 0.75

    # Xx and xx
    prob_dominant += (m / total) * (n / (total - 1)) * 0.5
    prob_dominant += (n / total) * (m / (total - 1)) * 0.5

    return prob_dominant

result =  round(get_prob_dominant(k, m, n), 5)
print('The probability that two random organisms produce dominant phenotype is:', result)
