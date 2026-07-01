# Problem 34: Error Correction in Reads.
# Uses two file paths. Adjust as necessary.

# Given a collection of up to 1000 reads of equal length in FASTA format.
# Wherein some of the reads contain a single-nucleotide error.

# Each read in s was either correctly sequenced and appears twice, 
# or incorrectly sequenced and appears once w/ a hamming distance of 1 from one other read.

# Return a list of all corrections in the form [old] -> [new] \n.

# 1. Define a function to get the hamming distance between any two reads.
def get_hamming_distance(read1, read2):
    distance = 0
    for a, b in zip(read1, read2):
        if a != b:
            distance += 1
    return distance

# 2. Define a function to get the reverse complement of a given read.
def get_rev_complement(read):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    c = [complements[letter] for letter in read]

    return ''.join(reversed(c))

# 3. Define a function to sift through incorrect reads to determine which read has 1 hamming distance from each incorrect read.
def find_corresponding_correct_reads(reads):
    # Find all incorrect reads.
    correct_reads = []
    for read in reads:
        rc = get_rev_complement(read)
        count = reads.count(read)
        if rc != read:
            count += reads.count(rc)
        if count > 1:
            correct_reads.append(read)
    incorrect_reads = [read for read in reads if read not in correct_reads]

    # Find correct reads that correspond to incorrect reads.
    corresponding_reads = {}
    for read1 in incorrect_reads:
        for read2 in correct_reads:
            if get_hamming_distance(read1, read2) == 1:
                corresponding_reads[read1] = read2
                break
            elif get_hamming_distance(read1, get_rev_complement(read2)) == 1:
                corresponding_reads[read1] = get_rev_complement(read2)
                break

    return corresponding_reads
    
# 4. Parse given file for list of reads. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_corr.txt'
with open(file_path, 'r') as f:
   reads = [line.strip() for line in f.readlines() if not line.startswith('>')]

# 5. Execute and print results. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_corr_output.txt'
corresponding_reads = find_corresponding_correct_reads(reads)
with open(file_path, 'w') as f:
    for old, new in corresponding_reads.items():
        f.write(f'{old}->{new}\n')
