with open('rosalind_kmp (1).txt') as data:
    seq = data.read()
    strings = sorted(seq.split('>'))

    str = []
    for index in strings:
        if(index!=""):
            strseq=index.split()
            str2=''.join(strseq[1:])
            str.append(str2)
            str = ', '.join(str)

    start_index = -1
    ref_result = [start_index]
    for index, value in enumerate(str):
        while start_index >= 0 and str[start_index] != value:
            start_index = ref_result[start_index]
        start_index += 1
        ref_result.append(start_index)

    for index in ref_result[1:]:
        print index,
