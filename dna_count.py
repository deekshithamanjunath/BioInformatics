#Question 2

with open('rosalind_dna.txt') as data:
    dnaSeq = data.read()
    seq = ['A', 'C', 'G', 'T']
    cnt = []
    for index in seq:
        a = dnaSeq.count(index)
        cnt.append(str(a))
print ' '.join(cnt)