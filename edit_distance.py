from numpy import zeros

with open ('rosalind_edit.txt') as input:
    data = input.read()
    strings = sorted(data.split('>'))

    str = []
    for index in strings:
        if(index!=''):
            strseq=index.split()
            str2=''.join(strseq[1:])
            str.append(str2)

seq1 = str[0]
seq2 = str[1]
len1 = len(seq1)
len2 = len(seq2)

matrixDist = zeros((len1+1,len2+1), dtype=int)

for index1 in range(1,(len1+1)):
    matrixDist[index1][0] = index1

for index2 in range(1,(len2+1)):
    matrixDist[0][index2] = index2

row = 1

while (row<(len1+1)):
    for col in range(1,(len2+1)):
        if(seq1[row-1] == seq2[col-1]):
            matrixDist[row][col] = matrixDist[row - 1][col - 1]
        else:
            matrixDist[row][col] = min(matrixDist[row - 1][col] + 1, matrixDist[row][col - 1] + 1, matrixDist[row - 1][col - 1] + 1)
    row += 1

print matrixDist[len1][len2]
