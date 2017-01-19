#Question 7

from Bio.Seq import translate

with open('rosalind_ptra.txt') as data:
	dna, protein = [lines.strip() for lines in data.readlines()]

for index in range(1,15):
    if index == 7:
        index = 8
    elif index == 8:
        index = 9
    elif translate(dna, table = index, stop_symbol = '', to_stop=False) == protein:
		codeVariant = str(index)
		break

print codeVariant




    j = 0
        percentage_gc = (count / len(list1)) * 100
        print percentage_gc
        init_dict1[j] = percentage_gc
        j+=1
        print init_dict1

j=0
    for i in input_dic:
        input_dic[i]=init_dict1[j]
        j+=1
    #print(init_dic)
    
    maxCount=max(init_dic,key=init_dic.get)

print(maxCount[1:])

print("%.6f"%init_dic[maxCount])

gc_values_dict = {}

for id, seq in input_dic.items():  # loop through input dictionary and get ID, sequence.
    gc_values_dict[id] = init_dict1(seq)  # calculate the GC value of each sequence and store it with ID.

max_gc_id = max(gc_values_dict, key=gc_values_dict.get)  # Get maximum value of the key

max_gc_value = max(gc_values_dict.values())  # Get maximum value of GC

# Print the values of Key and Value
print(max_gc_id)
print(round(max_gc_value, 7))


