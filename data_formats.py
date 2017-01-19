from Bio import SeqIO
from Bio import Entrez

with open('rosalind_frmt.txt') as data:
    inputId = data.read().strip().split()

control = Entrez.efetch(db='nucleotide', id=inputId, rettype='fasta')
file = list(SeqIO.parse(control, 'fasta'))

leastIndex = 0
for index in range(len(file)):
    for index2 in file:
        if len(file[index]) == min([len(index2.seq)]):
            leastIndex = index

control = Entrez.efetch(db='nucleotide', id=inputId, rettype='fasta')
shortestStrId = control.read().strip().split('\n\n')[leastIndex]

print shortestStrId
