with open('rosalind_cunr.txt')as input:
    num = int(input.read())

def mod(num):
    if num > 0:
        return num * mod(num - 2)
    else:
        return 1

print((mod(2 * num - 5) % 1000000))
