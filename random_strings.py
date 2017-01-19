from math import log10


with open('rosalind_prob.txt') as data:
    dnaSeq = data.readlines()
    
arrstring = dnaSeq[0]
arrcontent = map(float,dnaSeq[1].split(' '))

AT_content = arrstring.count('A') + arrstring.count('T')
CG_content = arrstring.count('C') + arrstring.count('G')
distribution = []

def prob(gc):
    at = 1 - gc
    probability = CG_content * log10(gc/2) + AT_content * log10(at/2)
    return probability

for value in arrcontent:
    print round(prob(value),3),

