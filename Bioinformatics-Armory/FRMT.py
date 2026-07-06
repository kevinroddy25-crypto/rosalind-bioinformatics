# Problem 3: Data Formats.
# Uses two file paths. Adjust as necessary.

# Given a collection of n GenBank entry IDs.
# Return the shortest of the strings associated with the IDs in FASTA format.

from Bio import Entrez
from Bio import SeqIO

# 1. Define a function to get the shortest of the given GenBank entry IDs.
def get_shortest_string_from_id(ids):
    Entrez.email = 'kevinroddy25@gmail.com'
    with Entrez.efetch(db='nucleotide', id=ids, rettype='fasta', retmode='text') as handle:
        records = list(SeqIO.parse(handle, 'fasta'))
    
    shortest_record = records[0]
    for record in records:
        if len(record.format('fasta')) < len(shortest_record.format('fasta')):
            shortest_record = record
    
    return shortest_record
    
# 2. Parse given file for GenBank IDs.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_frmt.txt'
with open(file_path, 'r') as f:
    ids = f.readline().strip().split(' ')

# 3. Execute and print results.
# Write in a separate file due to size. Adjust file path as necessary.
file_path = 'path/to/your/rosalind_frmt_output.txt'
with open(file_path, 'w') as f:
   SeqIO.write(get_shortest_string_from_id(ids), f, 'fasta')
