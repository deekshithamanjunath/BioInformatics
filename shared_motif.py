with open('rosalind_lcsm.txt') as data:
    seq = data.read()
    strings = sorted(seq.split('>'))
    
    str = []
    for index in strings:
        if(index!=""):
            strseq=index.split()
            str2=''.join(strseq[1:])
            str.append(str2)

    res = []
    for index in range(0,len(str)-1):
        str1 = str[index]
        str2 = str[index+1]
        len1 = len(str1)
        len2 = len(str2)
        matched_string = ""
        for i in range(len1):
            str_matches = ""
            for j in range(len2):
                if (i + j < len1):
                    if str1[i+j] == str2[j]:
                        str_matches +=str2[j]
                    else:
                        if (len(str_matches) > len(matched_string)):
                            matched_string = str_matches
                        str_matches = ""
    print matched_string








