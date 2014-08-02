#!/usr/local/bin/python3
'''
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

# listOfPrimes() function has been written to solve Problem 7
# now it is part of myUtils.py
from myUtils import listOfPrimes

# I didn't know what's better: to write my own function or to use an existing one?
# I decided to commit the solution that uses itertools module
# because my implementation wasn't using any new Python concepts,
# and my goal is to learn as much different things about Python as possible. 
from itertools import permutations

from sys import exit

primes = set (listOfPrimes (10000))

for p in primes:
    if p < 1000:
        continue # ignore 1-, 2-, and 3-digit primes
    
    perm = set ([])
    # add prime permutations to _perm_ set (no duplicates)
    for t in permutations(str(p)):
        if t[0] == '0':
            continue # ignore numbers with leading zero - not a valid 4-digit number
        ti = int("".join(t))
        if ti in primes:
            perm.update([ti])
    if len(perm) < 3:
        continue # ignore if less than 3 prime permutations 

    # convert _perm_ set to ordered list
    # to form a possible arithmetic sequence    
    perm = list (perm)
    perm.sort()

    # check all possible triplets
    limit = len(perm)
    for i in range (0, limit-2):
        for j in range (i+1, limit-1):
            for k in range (j+1, limit):
                if perm[i]+perm[k] == 2*perm[j]: # a[n] + a[n+2] = 2 * a[n+1] in arithmetic sequence
                    if perm[i] == 1487:
                        continue # ignore existing solution; optimal solution would break out of this nested loop 
                    else: # new solution found
                        print("Result:",str(perm[i])+str(perm[j])+str(perm[k]))                    
                        exit()
