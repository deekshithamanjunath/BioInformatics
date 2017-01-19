with open('test.txt') as input:
    dnaString = input.read().strip().split('\n')

strNum = int(dnaString[0])
gcCount = dnaString[2].split(" ")
expo = strNum - 1

for index in gcCount:
    gcContent = float(index)/2
    atContent = (1-float(index))/2
    gContent = dnaString[1].count("G")
    cContent = dnaString[1].count("C")
    aContent = dnaString[1].count("A")
    tContent = dnaString[1].count("T")
    print(round((gcContent ** gContent) * (gcContent ** cContent) * (atContent ** aContent) * (atContent ** tContent) * expo,3)),
