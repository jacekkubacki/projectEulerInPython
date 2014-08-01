#!/usr/local/bin/python3
'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

'''
Solution:
primeNumers is a list of prime numbers < n
To check if n is a prime number try to divide it by the elements of the primeNumber list.
If it is not possible then n is a prime number and add it to the list.
'''

import math

primeNumbers = [2]
n = 3 # start with 3 to skip all even numbers

while len(primeNumbers) < 10001:
    isPrime = True
    for p in primeNumbers[1:]: # ignore 2 as we are checking only odd numbers
        # we only want to check the primes <= sqrt(n)
        # see: http://en.wikipedia.org/wiki/Prime_number#Trial_division
        if p <= math.sqrt(n):
            if n % p == 0:
                isPrime = False
                break
        else:
            break
    if isPrime:
        primeNumbers.append(n)
    n += 2 # to skip even numbers

print ("Result:", primeNumbers[-1])
