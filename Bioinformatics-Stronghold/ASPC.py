# Problem 45: Introduction to Alternative Splicing.

# Given positive integers n and m with  0 ≤ m ≤ n ≤ 2000.
# Return the sum of combinations C(n,k) for al k satisfying m ≤ k ≤ n, modulo 10^6.

from math import comb

# 1. Define a function to get the sum of C(n,k) % 10^6 for m ≤ k ≤ n.
def get_sum_of_combinations(n: int, m: int):
    return sum(comb(n, k) for k in range(m, n + 1)) % 1000000

# 2. Get n and m as input.
n, m = map(int, input('Enter positive integers n and m separated by a space: ').strip().split(' '))

# 3. Execute and print results.
print(get_sum_of_combinations(n, m))
