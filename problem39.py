from Bio import Phylo
from io import StringIO
import re

def distance(inputTree, taxName):
    increase = 0
    decrease = 0
    
    taxName = taxName.split()
    tokens = iter(re.split('([(),])', inputTree))
    
    while next(tokens) not in taxName:
        pass
    
    for index in tokens:
        if index in taxName:
            break
        if index in ',)':
            if decrease > 0:
                decrease -= 1
            else:
                increase += 1

        
        if index in ',(':
            decrease += 1
    print(increase + decrease),



with open('rosalind_nwck.txt') as input:
    tree = [treeIn.split('\n') for treeIn in input.read().strip().split('\n\n')]

for key, val in tree:
    distance(key, val)
