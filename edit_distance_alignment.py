#Reference Biopython pairwise2 package.


from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

with open('rosalind_edta.txt') as inputData:
    protString = inputData.read().strip().split('>')

protList = []
for index in protString:
    if index != "":
        output = ''.join(index.split()[1:])
        protList.append(output)

align = pairwise2.align.localxx(protList[0], protList[1])

for index1 in align:
    out = format_alignment(*index1)
print out,

