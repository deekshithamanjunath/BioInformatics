#Question 10

with open('rosalind_mrna.txt') as data:
    mrnaSeq = data.read().strip()

    result=1
    proteinMap = {"A": 4, "C": 2, "D": 2, "E": 2,"G": 4 ,"H": 2,"F": 2, "I": 3, "K": 2, "L":6,
    "M": 1,"N": 2, "P":4, "Q": 2 , "R": 6 ,"S":6 ,"STOP":3 ,"T":4 , "V":4  , "Y": 2 ,"W":1}

    for index in range(len(mrnaSeq)):
        result = result * proteinMap[mrnaSeq[index]]
    
    result=result*3
    result = result % 1000000
print(result)
