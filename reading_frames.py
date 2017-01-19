from Bio.Seq import Seq
from Bio.Seq import translate


with open('rosalind_orf.txt') as data:
    dnaSeq = data.read().splitlines()
    dnaSeq = ''.join(dnaSeq[1:])
    stringReverse = str(Seq(dnaSeq).reverse_complement())


array_position  = []
array_reverse = []

def string_conv(input):
    pos = []
    index = 0
    while index < len(input):
        if input[index:index+3] == "ATG":
            pos.append(index)
        index += 1
    return pos

def seq_array_position(input_position,in_string):
    seq_array = []
    for index in input_position:
        seq_array.append(translate(in_string[index:],table = 'Standard',to_stop = False))
    return seq_array

array_position = string_conv(dnaSeq)
array_reverse = string_conv(stringReverse)

seq_final = seq_array_position(array_position,dnaSeq)+seq_array_position(array_reverse,stringReverse)

dict = {}

for index in seq_final:
    if '*' in index:
        dict[index[:index.find('*')]]=0

for key in dict.keys():
    print key
