from Bio import SeqIO

with open('rosalind_tfsq.txt') as inputInfo, open('out.txt', 'w') as outputInfo:
    SeqIO.convert(inputInfo, 'fastq', outputInfo, 'fasta' )

