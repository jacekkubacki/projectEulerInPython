#!/usr/bin/env python3

# Sub-string divisibility
# Problem 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# Solution:
# We are going to use some more efficient division properties:
#     d2d3d4=406 is divisible by 2 -> d4 must be divisible by 2
#     d3d4d5=063 is divisible by 3 -> the sum of the digits (d3+d4+d5) must be divisible by 3
#     d4d5d6=635 is divisible by 5 -> d6 must be divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17

from itertools import permutations


def calculate_decimal_value(digits):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * 10 + digit
    return decimal_value


result = 0
for number in permutations(range(10)):
    # d2d3d4=406 is divisible by 2 -> d4 must be divisible by 2
    if number[4-1] % 2:
        continue
    # d3d4d5=063 is divisible by 3 -> the sum of the digits (d3+d4+d5) must be divisible by 3
    if sum(number[3-1:5]) % 3:
        continue
    # d4d5d6=635 is divisible by 5 -> d6 must be divisible by 5
    if number[6-1] % 5:
        continue
    # d5d6d7=357 is divisible by 7
    d5d6d7 = calculate_decimal_value(number[5-1:7])
    if d5d6d7 % 7:
        continue
    # d6d7d8=572 is divisible by 11
    d6d7d8 = calculate_decimal_value(number[6-1:8])
    if d6d7d8 % 11:
        continue
    # d7d8d9=728 is divisible by 13
    d7d8d9 = calculate_decimal_value(number[7-1:9])
    if d7d8d9 % 13:
        continue
    # d8d9d10=289 is divisible by 17
    d8d9d10 = calculate_decimal_value(number[8-1:10])
    if d8d9d10 % 17:
        continue

    result += calculate_decimal_value(number)

print(f"Result: {result}")
