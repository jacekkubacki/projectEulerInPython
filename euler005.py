#!/usr/local/bin/python3
'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Soltion:
What we are looking for is a lowest common multiple of 1..20.
See: http://en.wikipedia.org/wiki/Least_common_multiple#Finding_least_common_multiples_by_prime_factorization
'''

# primeFactorization() function has been written to solve Problem 3
# now it is part of myUtils.py in case I'll be needing it in the future

from myUtils import primeFactorization
from collections import Counter

factors = Counter()

for n in range (1, 20 + 1):
    f = Counter (primeFactorization(n))
    # to make sure 'f' factors are added correctly to 'factors':
    # remove the ones that are already in 'factors' first
    # and then re-add them along with (possibly) new ones
    factors = (factors - f) + f 

result = 1
for e in list(factors.elements()):
    result *= e

print ("Result:", result)
