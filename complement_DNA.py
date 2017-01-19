#Question 5

from Bio.Seq import Seq

def reverseComplement(input1):
    dnaRev = input1.reverse_complement()
    print dnaRev
    return dnaRev

with open('rosalind_revc.txt') as data:
    dnaSeq = Seq(data.read())
outputSeq = reverseComplement(dnaSeq)