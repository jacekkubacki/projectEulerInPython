#!/usr/bin/env python3

# Circular primes
# Problem 35
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

# Solution:
# Find all the prime numbers < 1000000 first.
# Then for each prime:
# - ignore it if it is already in the 'circularPrimes' set
# - if all the rotations are in the 'primes' set then add all of them to 'circularPrimes' set

from myUtils import listOfPrimes


def listOfRotations (n):
    if 0 in set(list(str(n))):
        return [] # cannot rotate numbers containing '0'
    result = []
    s = str(n)
    for i in range(0, len(s)):
        result.append(int(s))
        s = s[1:]+s[0]
    return result
    
circularPrimes = set([])
primes = set(listOfPrimes(1000000))

for p in primes:
    if p in circularPrimes:
        continue

    isCircular = True
    for i in listOfRotations(p):
        if i not in primes:
            isCircular = False
            break 
    if isCircular:
        circularPrimes.update(listOfRotations(p))
        
print ("Result:", len(circularPrimes))
