#!/usr/local/bin/python3
'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime (n):
    # This algorithm will check only numbers of the form 6k ± 1
    # see: http://en.wikipedia.org/wiki/Primality_test#Naive_methods
    if n <= 3:
        return n <= 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range (5, int(n**0.5) + 1, 6):   
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

primesFound = 2 # 2, 3
n = 3

while primesFound < 10001:
    n += 2
    if isPrime(n):
        primesFound += 1

print ("Result:", n)
