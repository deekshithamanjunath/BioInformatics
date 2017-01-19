
with open('rosalind_tree.txt') as data:
    input = data.readlines()

nodes = []
for num in input:
    nodes.append(map(int,num.rstrip().split()))
n = nodes[0][0] - 1
print (n-len(nodes[1:]))
