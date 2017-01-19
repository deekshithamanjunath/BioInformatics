def charSpecies(set, charac):
    if len(set) == 1:
        return int(charac[set[0]])
    arr = [[], []]

    for input in set:
        z = charSpecies(input, charac)
        if z == -1:
            return -1
        else:
            arr[z].append(input)

    if len(arr[1]) == 0:
        return 0
    elif len(arr[0]) == 0:
        return 1
    else:
        set[:] = []
        set.append(arr[1])
        set.extend(arr[0])
        return -1

def treeMatrix(input):
    if input[0] == '0':
        return input
    else:
        return ''.join([str(1 - int(key)) for key in input])

def output(edge):
    if len(edge) == 1:
        return taxonomy[edge[0]]
    else:
        s = ''
        for treeMatrix in edge:
            s += output(treeMatrix)
            s += ','
    return '(%s)' % (s[:-1])


with open('rosalind_chbp.txt') as inputData:
    taxName = inputData.readline().split()
    characs = [treeMatrix(num.strip()) for num in inputData.readlines()]

taxonomy = dict(zip(range(len(taxName)), taxName))
result = [[index] for index in range(len(taxName))]

for name in characs:
    charSpecies(result, name)

print(output(result))
