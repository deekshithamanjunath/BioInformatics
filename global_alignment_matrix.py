from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

list = matlist.blosum62

with open('rosalind_glob.txt') as data:
    protString = data.read().strip().split('>')

protList = []
for index in protString:
    if index != "":
        output = ''.join(index.split()[1:])
        protList.append(output)

alignment = pairwise2.align.globalds(protList[0], protList[1], list, -5, -5)

for index in alignment:
    print(format_alignment(*index))
