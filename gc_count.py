with open('rosalind_gc.txt') as data:
    dnaSeq = data.readlines()
    
    result = {}
    i=0
    arr = []
    for line in dnaSeq:
        arr.append(line.rstrip())
        i = i+1

    dict1 = {}
    dictKey = ''

    for index in arr:
        if index[0] == '>':
            dictKey = index[1:].rstrip()  # removes all whitespace and new line from input.
            dict1[dictKey] = ''  # store the key as reference. Value can be stored next.
        
        else:
            # store values in corresponding keys
            dict1[dictKey] = dict1[dictKey] + index.rstrip()
    print dict1

    for index1 in range(len(dict1)):
        list1= dict1.values()
    print list1

    dict2={}
    gcCount = 0
    j = 0
    for i in list1:
        gcCount= i.count("C") + i.count("G")
        result= (gcCount/float(len(i)))
        result=result*100
        result=float(result)
        dict2[j]=result
        j+=1

    x=0
    for i in dict1:
        dict1[i] = dict2[x]
        x= x+1
    print(dict1)

    maxresultkey = dict1.keys()[0]
    maxresultvalue = dict1.values()[0]
    for key in dict1:
        if dict1[key] > maxresultvalue:
            maxresltkey = key
            maxresultvalue = dict1[key]

print maxresultkey
#print round(maxresultvalue,6)
print("%.6f"%init_dic[maxCount])