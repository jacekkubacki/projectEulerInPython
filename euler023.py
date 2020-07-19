#!/usr/bin/env python3

# Non-abundant sums
# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from bisect import bisect

from my_utils import arithmetic_sum, list_of_divisors

# no need to check numbers >= 28123
limit = 28123

abundant_numbers = []
# find all abundant numbers < limit, 12 is the smallest one
for n in range(12, limit):
    if sum(list_of_divisors(n)) > n:
        abundant_numbers.append(n)

# using 'set' to make sure sums are unique
sum_of_two_abundants = set()
# find all sums of two abundant numbers
for i in range(0, len(abundant_numbers)):
    # add only numbers >= abundant_numbers[i]
    # bisect() is used to make sure the sum < limit
    for j in range(i, bisect(abundant_numbers, limit - abundant_numbers[i])):
        sum_of_two_abundants.add(abundant_numbers[i] + abundant_numbers[j])

sum_of_all_numbers = int(arithmetic_sum(1, 1, limit))

# The sum of all the positive integers which cannot be written as the sum of two abundant numbers
# equals to the sum of all numbers from 1 to 28123
# minus the sum of all the positive integers which CAN be written as the sum of two abundant numbers.
print("Result:", sum_of_all_numbers - sum(sum_of_two_abundants))
