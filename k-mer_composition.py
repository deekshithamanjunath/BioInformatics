from itertools import product

with open('rosalind_kmer.txt') as data:
    dnaSeq = data.read().splitlines()
sequence = ''

sequencestring = []
dict = {}
stringArray = []

sequencelist = list(product('ATCG',repeat = 4))
sequencestring  = (map(''.join,sequencelist))
sequencestring.sort()

for index in range(1,len(dnaSeq)):
    sequence += dnaSeq[index]

for index in range(1,len(sequence)-2):
    stringArray.append(sequence[index:index+4])

for index in sequencestring:
    dict[index]=stringArray.count(index)

for index in sorted(dict):
    print dict[index],
