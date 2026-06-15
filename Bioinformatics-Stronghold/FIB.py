# Problem 4: Rabbits and recurrence relations.

# Given: Positive integers n and k. Adjust file path as needed.
file_path = 'path/to/your/rosalind_fib.txt'

with open(file_path, 'r') as f:
    n, k = map(int, f.read().strip().split())

# Return the total number of rabbit pairs present after n months,
# Where k is the number of rabbit pairs produced by each reproductive pair in a month.

# Assume that rabbits reach reproductive age after one month.
# Assume that, in any given month, every rabbit of reproductive age mates w/ another rabbit and produces a litter of k rabbit pairs.
# Assume that rabbits are immortal and perpetually fertile.

# Recursive functions reference themselves.
def get_rabbit_pairs(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return get_rabbit_pairs(n - 1, k) + k * get_rabbit_pairs(n - 2, k)

pairs = get_rabbit_pairs(n, k)
print(str(pairs))
