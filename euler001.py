#!/usr/bin/env python3

# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Solution:
# Instead of using a loop we can simply find the sums of arithmetic progressions
# http://en.wikipedia.org/wiki/Arithmetic_progression
# Just add the sum for multiplies of 3 and sum for multiplies of 5 and subtract sum for multiplies of 15
# (because numbers such as 15 have been added twice: as a multiply of 3 and as a multiply of 5)

from my_utils import arithmetic_sum

limit = 1000

s3 = arithmetic_sum(3, 3, (limit - 1) // 3)
s5 = arithmetic_sum(5, 5, (limit - 1) // 5)
s15 = arithmetic_sum(15, 15, (limit - 1) // 15)

print("Result:", int(s3 + s5 - s15))
