from Bio.Seq import Seq

with open('rosalind_dbru.txt') as input:
    dnaStrs = input.readlines()

strArr = []
strArrRev = []
list1 = []
list2 = []

for index in dnaStrs:
    strArr.append(index.strip())

for index in strArr:
    element = Seq(index)
    strArrRev.append("%s" %element.reverse_complement())

for index in range(len(strArr)):
    rev = strArrRev[index][:-1]
    string = strArrRev[index][1:]
    revStr = (rev,string)
    list2.append(revStr)

for index in range(len(strArr)):
    element1 = strArr[index][:-1]
    element2 = strArr[index][1:]
    element = (element1,element2)
    list1.append(element)

out = set(list1)
out.update(list2)

for (index1,index2) in sorted(out):
    print '(%s, %s)' %(index1,index2)

