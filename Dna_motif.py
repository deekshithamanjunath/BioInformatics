with open('rosalind_subs.txt') as data:
    strg = data.readline().strip()
    substr = data.readline().strip()

substr_location = []
for i in range(len(strg)):
    if strg[i:i + len(substr)] == substr:
        substr_location.append(str(i+1))

print ' '.join(substr_location)

