# Problem 11: Mortal Fibonacci rabbits.

# Given + integers n and m.
given = input('Enter two integers, n and m: ')
integers = given.split(' ')

n = int(integers[0])
m = int(integers[1])

# Use DYNAMIC PROGRAMMING, rather than naive recursion (see problem 4).
def get_rabbit_pairs(n: int, m: int):
    # We begin with 1 pair of rabbits.
    if n <= 0:
        return 0
    
    # Track the number of pairs born in each month. Index represents the month. We initialize up to month 'n'.
    births = [0] * (n + 1)
    
    # In month 1, we start with 1 newborn pair of rabbits.
    births[1] = 1
    
    # Iterate through each month from 2 up to n
    for i in range(2, n + 1):
        # 1. Count how many total pairs are alive in the previous month (i - 1) to find out how many are mature enough to reproduce.
        # Mature pairs = Total alive in (i-1) minus newborns born in (i-1).
        
        # To get total alive in a month, we sum births from (current_month - m + 1) to current_month
        alive_prev_month = sum(births[max(1, i - 1 - m + 1) : i])
        newborns_prev_month = births[i - 1]
        
        reproducing_pairs = alive_prev_month - newborns_prev_month
        
        # Each reproducing pair produces 1 new pair
        births[i] = reproducing_pairs
        
    # Total pairs remaining after the n-th month are those born between (n - m + 1) and n
    start_index = max(1, n - m + 1)
    total_remaining_pairs = sum(births[start_index : n + 1])
    
    return total_remaining_pairs

print("Answer:", get_rabbit_pairs(n, m))
