#!/usr/bin/env python3

# Power digit sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

from my_utils import sum_of_digits

print("Result:", sum_of_digits(pow(2, 1000)))
