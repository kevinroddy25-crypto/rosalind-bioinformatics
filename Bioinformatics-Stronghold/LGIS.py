# Problem 24: Longest Increasing Subsequence.
# Uses two file paths. Adjust as necessary.

# Given a positive integer n, followed by a permutation pi of length n.
# Return a longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.
import bisect

# 1. Find the longest increasing subsequence using patience sorting algorithm.
def find_longest_increasing_subsequence(sequence):
    """Compute the longest strictly increasing subsequence using binary search."""
    active_piles = []
    pile_indices = []
    previous_element_index = [-1] * len(sequence)

    for current_index, element_value in enumerate(sequence):
        # Find position where element should go to maintain sorted order
        insertion_position = bisect.bisect_left(active_piles, element_value)
        if insertion_position == len(active_piles):
            active_piles.append(element_value)
            pile_indices.append(current_index)
        else:
            active_piles[insertion_position] = element_value
            pile_indices[insertion_position] = current_index
        if insertion_position > 0:
            previous_element_index[current_index] = pile_indices[insertion_position - 1]

    reconstructed_subsequence = []
    if pile_indices:
        current_index = pile_indices[-1]
        while current_index != -1:
            reconstructed_subsequence.append(sequence[current_index])
            current_index = previous_element_index[current_index]
    return reconstructed_subsequence[::-1]

# 2. Find the longest decreasing subsequence by reversing and finding LIS.
def find_longest_decreasing_subsequence(sequence):
    """Compute the longest strictly decreasing subsequence by processing reversed sequence."""
    reversed_sequence = sequence[::-1]
    active_piles = []
    pile_indices = []
    previous_element_index = [-1] * len(sequence)

    for current_index, element_value in enumerate(reversed_sequence):
        insertion_position = bisect.bisect_left(active_piles, element_value)
        if insertion_position == len(active_piles):
            active_piles.append(element_value)
            pile_indices.append(current_index)
        else:
            active_piles[insertion_position] = element_value
            pile_indices[insertion_position] = current_index
        if insertion_position > 0:
            previous_element_index[current_index] = pile_indices[insertion_position - 1]

    reconstructed_subsequence = []
    if pile_indices:
        current_index = pile_indices[-1]
        while current_index != -1:
            reconstructed_subsequence.append(reversed_sequence[current_index])
            current_index = previous_element_index[current_index]
            
    return reconstructed_subsequence

# 3. Read input data from Rosalind file.
# Adjust file path as necessary.
input_file_path = 'path/to/your/rosalind_lgis.txt'
with open(input_file_path, 'r') as input_file:
    sequence_length = int(input_file.readline().strip())
    permutation_sequence = list(map(int, input_file.readline().strip().split()))

# 4. Calculate longest increasing and decreasing subsequences.
longest_increasing_result = find_longest_increasing_subsequence(permutation_sequence)
longest_decreasing_result = find_longest_decreasing_subsequence(permutation_sequence)

# Adjust file path as necessary.
output_file_path = 'path/to/your/rosalind_lgis_output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(' '.join(map(str, longest_increasing_result)) + '\n')
    output_file.write(' '.join(map(str, longest_decreasing_result)))

print(f'Executed! Open {output_file_path} and copy output.')
