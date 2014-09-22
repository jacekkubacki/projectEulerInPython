#!/usr/local/bin/python3
'''
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?
'''

from myUtils import primeFactors

n = 2 * 3 * 5 * 7 - 1

factors = []


while True:
    n += 1
    f = primeFactors(n)

    if len(set(f)) == 4:
        factors += f

        # check n+1, n+2 and n+3
        for c in [n + 1, n + 2, n + 3]:
            x = primeFactors(c)
            if len(set(x)) == 4:
                factors += x
            else:
                factors = []
                break

            if len(set(factors)) == 4*4:
                print("Result:", n)
                break


'''
while True:

    if len(Counter(primeFactors(n))) == 4:
        # check n+1, n+2 and n+3
        consecutive = True
        for c in [n+1,n+2,n+3]:
            if len(Counter(primeFactors(c))) != 4:
                consecutive = False
                break
        
        if consecutive:
            factors = []
            for d in [n, n+1, n+2, n+3]:
                p = Counter(primeFactors(d))
                for b in p.keys():
                    factors.append(b**p[b])

            if len(set(factors)) == 4*4:
                print(n)
                break
    n += 1
'''

'''
 134043
 '''
        


