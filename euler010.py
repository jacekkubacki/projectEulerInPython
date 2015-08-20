#!/usr/bin/env python3

# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from myUtils import listOfPrimes

print ("Result:", sum(listOfPrimes(2000000)))
