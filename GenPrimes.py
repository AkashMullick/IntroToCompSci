'''
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Note that the test cases show calls <generator>.next(). In Python 3, this is actually <generator>.__next__().
'''

def genPrimes():
    primeList = []
    last = 1
    while True:
        last += 1
        for p in primeList:
            if last % p == 0:
                break
        else:
            primeList.append(last)
            yield last
