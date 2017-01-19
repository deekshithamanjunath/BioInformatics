from Bio import SwissProt
from Bio import ExPASy


with open('rosalind_dbpr.txt') as data:
    protId = data.read().strip()

control = ExPASy.get_sprot_raw(protId)
file = SwissProt.read(control)
fileList = file.cross_references

output = []
for index in fileList:
    if index[0] == 'GO' and index[2][0]=='P':
        output.append(index[2].lstrip('P:'))

for index in output:
    print index
