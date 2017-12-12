#!/usr/bin/env python3

# Pandigital prime
# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# Solution:
# For every 5-, 6-, 8- and 9-digit pandigital number the sum of digits is divisible by 3, so the number itself is divisible by 3, see:
# http://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9
# So it is enough to check 7- and 4-digit pandigital numbers (2143 is a 4-digit prime pandigital number).

from itertools import permutations
from my_utils import is_prime
import sys

for n in [7, 4]:
    # generate list of digits in a descending order, to make sure permutations start from the biggest number
    digits = "".join([str(i) for i in range (n, 0, -1)])

    for number in [int(''.join(p)) for p in permutations(digits)]:
        if is_prime(number):
            print ("Result:", number)
            sys.exit()
