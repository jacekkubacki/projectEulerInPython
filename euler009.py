#!/usr/bin/env python3

# Special Pythagorean triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Solution:
# Let c be the hypotenuse, the longest side of the right-angled triangle.
# It cannot be shorter than 334 to be the longest side.
# It cannot be longer than 500 to make sure a, b and can form a triangle (c < a + b).
# Let b be the longer cathetus.
# It cannot be shorter than (1000 - c) / 2 to be longer than a.
# It cannot be longer than c.
# Let a be the shorter cathetus.
# a = 1000 - b - c


class BreakInnerLoop(Exception):
    pass


try:
    for c in range(334, 500):
        for b in range(c, (1000-c)//2, -1):
            a = 1000 - c - b
            if c * c == a * a + b * b:
                print("Result:", a*b*c)
                raise BreakInnerLoop
except BreakInnerLoop:
    pass
