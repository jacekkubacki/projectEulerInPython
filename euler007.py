#!/usr/local/bin/python3
'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from myUtils import isPrime

primesFound = 2 # 2, 3
currentNumber = 3

while primesFound < 10001:
    currentNumber += 2
    if isPrime(currentNumber):
        primesFound += 1

print ("Result:", currentNumber)
