with open('rosalind_ba9j.txt') as data:
    revStr = data.read().strip()


revTransform = list(revStr)
revTransform_sorted = sorted(revTransform)
length = len(revTransform)

revTransform_sorted = [revTransform[element] + revTransform_sorted[element] for element in range(0, length)]
revTransform_sorted.sort()

for index in range(1, length - 1):
    revTransform_sorted = [revTransform[element] + revTransform_sorted[element] for element in range(0, length)]
    revTransform_sorted.sort()

for index in range(0, len(revTransform_sorted)):
    if revTransform_sorted[index][-1] == '$':
        inputStr = revTransform_sorted[index]

print inputStr
