# Problem 15: Independent Alleles.

# Given: Two positive integers k ≤ 7 and N ≤ 2k.
# In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
# Tom has two children in the 1st generation, each of whom has two children, and so on. 
# Each organism always mates with an organism having genotype Aa Bb.


# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation
# of Tom's family tree (don't count the Aa Bb mates at each level). 
# Assume that Mendel's second law holds for the factors.

import math

# 1. Define a function to get the probability that at least N AaBb organisms belong to the k-th generation.
def get_prob_AaBb(k, N):
    # Binomial distribution formula: P(X = x) = (n!/(x!(n-x)!))p^x(1-p)^(n-x)
    # Solves for the probability of x successes out of n trials.
    # (n!/(x!(n-x)!)) is the formula for the probability of a combination.

    p = 0.25
    n = 2 ** k

    sum_probs = 0
    for x in range(N, n + 1):
        sum_probs += (math.comb(n, x)) * p ** x * (1 - p) ** (n - x)

    return round(sum_probs, 3)

# 2. Parse input for k and N.
k, N = map(int, input('Enter two positive integers k and N: ').split(' '))

# 3. Execute and print results.
print(get_prob_AaBb(k, N))
