import numpy as np

with open('rosalind_cons.txt') as data:
    seq = data.read()
    strings = sorted(seq.split('>'))
    
    sequence = []
    for index in strings:
        if(index!=""):
            strseq=index.split()
            str2=''.join(strseq[1:])
            sequence.append(str2)


strlength = len(sequence)

profileMatrix = []
for index in sequence:
    profileMatrix.append([element for element in index])

lenprofile = len(profileMatrix)
lenprofile1 = len(profileMatrix[0])
arr = np.array(profileMatrix).reshape(lenprofile,lenprofile1)

A = []
T = []
C = []
G = []


for index in range(lenprofile1):
    Acnt = 0
    Tcnt = 0
    Ccnt = 0
    Gcnt = 0
    for index1 in arr[:,index]:
        if index1 == "A":
            Acnt += 1
        elif index1 == "T":
            Tcnt += 1
        elif index1 == "C":
            Ccnt += 1
        elif index1 == "G":
            Gcnt += 1

    A.append(Acnt)
    T.append(Tcnt)
    C.append(Ccnt)
    G.append(Gcnt)

countMatrix = []

countMatrix.append(A)
countMatrix.append(T)
countMatrix.append(C)
countMatrix.append(G)

profile = np.array(countMatrix).reshape(4, len(T))

group = []
for index in range(len(T)):
    if max(profile[:,index]) == profile[0,index]:
        group.append("A")
    elif max(profile[:,index]) == profile[1,index]:
        group.append("T")
    elif max(profile[:,index]) == profile[2,index]:
        group.append("C")
    elif max(profile[:,index]) == profile[3,index]:
        group.append("G")
print "".join(group)

print "A:"
for i in profile[0]:
    print i,
print
print "C:"
for i in profile[1]:
    print i,
print
print "G:"
for i in profile[2]:
    print i,
print
print "T:"
for i in profile[3]:
    print i,





