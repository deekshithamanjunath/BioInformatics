from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

list = matlist.blosum62

with open('rosalind_gaff.txt') as data:
    protString = data.read().strip().split('>')

protList = []
for index in protString:
    if index != "":
        output = ''.join(index.split()[1:])
        protList.append(output)

alignment = pairwise2.align.globalds(protList[0], protList[1], list, -11, -1)

for index in alignment:
    print(format_alignment(*index))
