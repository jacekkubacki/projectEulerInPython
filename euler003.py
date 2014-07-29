#!/usr/local/bin/python3
'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def primeFactorization (n):
    # all the prime factors that are < n are also <= sqrt(n)
    limit = int (math.sqrt(n))

    while limit > 0:
        # factors found        
        if n % limit == 0:
            # if limit == 1 then n must be prime
            if limit == 1:
                return [n]
            # try to factorize the factors found
            else:
                return primeFactorization(limit) + primeFactorization(n//limit)
        limit -= 1

print ("Result:", max(primeFactorization(600851475143)))

