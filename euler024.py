#!/usr/local/bin/python3
'''
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
Solution:

There are 9! = 362880 permutations starting with 0, so the last one (0987654321) has index 362880.
The last permutation starting with 1 has index = 2 * 9! < 1,000,000.
The last permutation starting with 2 has index = 3 * 9! > 1,000,000 so the number we are looking for starts with 2.

There are 8! = 40320 permutations starting with 20, the last one has index 2 * 9! + 8! < 1,000,000
There are 8! = 40320 permutations starting with 21, the last one has index 2 * 9! + 2 * 8! < 1,000,000
And so on...
'''

from math import factorial

remainingDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 1000000  # index of a permutation we are looking for
currentIndex = 1
result = []

for n in range(9, -1, -1):
    # start with the first digit in 'remainingDigits'
    digitIndex = 0
    # there are n! permutation with that digit on current position
    f = factorial(n)

    while currentIndex + f <= index:
        # the permutation we are looking for doesn't use the current digit on current position
        # update the index
        currentIndex += f
        # and check the next digit
        digitIndex += 1

    # add current digit to 'result'
    result.append(remainingDigits[digitIndex])
    # and remove it from 'remainingDigits' as it will not be used again
    del remainingDigits[digitIndex]

print ("Result:", ''.join(map(str, result)))
