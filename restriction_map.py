from math import sqrt

with open('rosalind_pdpl.txt') as inputSet:
    inputMultiset = map(int,inputSet.read().strip().split())

setX = [0]
num = int(0.5 + 0.5 * sqrt(8.0 * len(inputMultiset) + 1))

setX.append(max(inputMultiset))
inputMultiset.remove(setX[1])

deltaSetX = set(inputMultiset)

element = 1
while element < deltaSetX:
    if sum([(abs(element - member) in inputMultiset) for member in setX]) == len(setX):
        for member in setX:
            inputMultiset.remove(abs(element - member))
        setX.append(element)
    element += 1
    
    if len(setX) == num: break
setX.sort()
print ' '.join(map(str, setX))
