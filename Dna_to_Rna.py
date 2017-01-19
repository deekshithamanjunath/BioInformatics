#Question 8

import re
with open('rosalind_rna.txt') as data:
    DNA_to_RNA = data.read()
    DNA_to_RNA=re.sub("T","U",DNA_to_RNA)
print DNA_to_RNA