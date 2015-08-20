#!/usr/bin/env python3

# Pandigital multiples
# Problem 38
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Solution:
# If the number we are looking for exists then it must be bigger than 918273645, so it must start with 9.
# For 2-, 3- and 5-, 6- or more digits numbers starting with 9 the concatenated product with (1,2,..) never has 9 digits,
# so we will check 4-digit numbers (starting with 9) only.

from itertools import permutations

result = "918273645"  # in case this is the largest one

# permutations are sorted if the iterable ("87654321") is sorted
# starting with "9876" to break out of the loop as soon as the first solution is found
for number in ['9'+''.join(p) for p in permutations("87654321",3)]:
    newNumber = number + str(int(number)*2)  # concatenate number x 1 and number x 2, 9 digits
    if len(set('0' + newNumber)) == 10:  # '0' added to rule out numbers containing '0', e.g. 935218704
        result = newNumber
        break

print ("Result:", result)
