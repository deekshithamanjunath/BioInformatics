with open('rosalind_fib.txt') as data:
    dnaSeq = data.read()
    dnaSeq = dnaSeq.split(' ')

month = int(dnaSeq[0])
rabbitpair = int(dnaSeq[1])

def fib_rabbitcount(month, rabbitpair):
    if month == 1 or month == 2:
        return 1
    else:
        count = (rabbitpair * fib_rabbitcount((month - 2), rabbitpair))+ fib_rabbitcount(month - 1, rabbitpair)
    return count

print fib_rabbitcount(month, rabbitpair)

