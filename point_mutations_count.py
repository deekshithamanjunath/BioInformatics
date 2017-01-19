with open('rosalind_hamm.txt') as input:
    data = input.read().split()
hamDist = 0
cnt = 0

seq1 = data[0]
seq2 = data[1]
length = len(seq2)

while (cnt < length):
    if (seq2[cnt] != seq1[cnt]):
        hamDist += 1
    cnt += 1

print(hamDist)
