from itertools import product

with open('rosalind_lexf.txt') as data:
    dnaSeq = data.readlines()

prod = product(dnaSeq[0].split(),repeat = int(dnaSeq[1]))
sequence = map(''.join,list(prod))
sequence.sort()

for index in sequence:
    print index
