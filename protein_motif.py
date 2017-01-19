import urllib

with open('rosalind_mprt.txt') as data:
    data = data.read().splitlines()
    
for protein_name in data:
    uri = "http://www.uniprot.org/uniprot/"+protein_name+".fasta"
    protein_fasta = urllib.urlopen(uri)
    list= protein_fasta.read().splitlines()
    position = ''
    for i in list[1:]:
        position +=i
    
    locations = []
    for i in range(0, (len(position))-4):
        if (position[i] == 'N') and (position[i+1] != 'P') and (position[i+2] in ['S', 'T']) and (position[i+3] != 'P'):
            locations.append(position[i:i+4])

    if len(locations) > 0:
        print protein_name
        for index in locations:
            print position.find(index)+1,
    print


