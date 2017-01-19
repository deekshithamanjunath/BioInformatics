import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
from Bio.SubsMat import MatrixInfo as matlist

with open('rosalind_laff.txt') as data:
    input = data.read().strip().split('>')
    print input

list = []
for word in input:
    if len(word) > 0:
        out = ''.join(protein.split()[1:])
        list.append(out)

matrix = matlist.blosum62

for value in pairwise2.align.localds(protein[0], protein[1], matrix, -11, -1):
    print(format_alignment(*value))

#Reference Biopython's pairwise2 package and Blosum62 matrix
