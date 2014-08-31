#!/usr/local/bin/python3
'''
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from myUtils import listOfPrimes

limit = 1000000
primeList = listOfPrimes(limit)
primeSet = set (primeList)

maxSize = 21 # 21 consecutive primes...
maxPrime = 953 # ...add up to 953

start = 0 # index of the first element
length = len(primeList)
size = maxSize # minimum size of the sublist

# Scan through the list of primes
while start + maxSize <= length:
    s = sum(primeList[start:start+size])

    if s >= limit: # sum is too big, reset _size_ and start from the next prime
        start += 1
        size = maxSize
        continue
        
    if s in primeSet:
        if maxPrime < s: # new longest sum found
            maxPrime = s
            maxSize = size

    size += 1 # try longer subset   
    
print ("Result:", maxPrime)
