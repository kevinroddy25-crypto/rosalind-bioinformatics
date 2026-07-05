# Problem 2: GenBank Introduction.
# Uses one file path and one email address. Adjust as necessary.

# Given a genus name followed by two dates in YYYY/M/D format.
# Return the number of nucleotide GenBank entries for the given genus that were published between
# the specified dates.

from Bio import Entrez
from typing import Any, Dict, cast

# 1. Define a function to search GenBank for a given genus between dates.
def get_num_entries_for_genus(genus: str, date1, date2):
    # Adjust email address as necessary.
    Entrez.email = 'your.email@org.com'
  
    search_term = f'{genus}[Organism] AND ({date1}:{date2}[PDAT])'
    with Entrez.esearch(db='nucleotide', idtype='acc', term=search_term) as handle:
        record = cast(Dict[str, Any], Entrez.read(handle))
    return int(record['Count'])

# 2. Parse given file for genus, date1, and date2.
# Adjust file path as necessary.
file_path = 'path/to/your/rosalind_gbk.txt'
with open(file_path, 'r') as f:
    genus, date1, date2 = [line.strip() for line in f.readlines() if line.strip()]

# 3. Execute and print results.
print(get_num_entries_for_genus(genus, date1, date2))
