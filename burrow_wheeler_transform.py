from collections import deque

with open('rosalind_ba9i.txt') as input:
    inputStr = input.read().strip()

transformMatrix = []
transformMatrix.append(inputStr)

queue = deque(inputStr)

transformRotation = []

for index in range(0,len(queue)):
    transformRotation.append(''.join(map(queue.rotate(-1),queue)))

for index in range(0,len(transformRotation)-1):
    transformMatrix.append(transformRotation[index])

transformMatrix.sort()
burTransformation = ""
for index in range(0,len(transformMatrix)):
    burTransformation = burTransformation + transformMatrix[index][-1:]

print burTransformation
