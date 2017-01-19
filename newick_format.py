from StringIO import StringIO
from Bio import Phylo

with open('rosalind_nkew.txt') as inputData:
    data = inputData.read().strip().split('\n\n')

arrList = []
for index in data:
    arrList.append(index.split('\n'))

for edge, weight in arrList:
    name, num = weight.split()
    tree = Phylo.read(StringIO(edge), 'newick')
    print(int(tree.distance(name,num))),
