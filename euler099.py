#!/usr/bin/env python3

# Largest exponential
# Problem 99
#
# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
#
# However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.

# Solution:
# Natural logarithm (ln) can be used to compare big numbers, because it is monotonically increasing function, and ln(a^b) = b * ln(a)

from math import log

result = 0  # line number with the greatest value
largestNumber = 0
lineNumber = 1

f = open('p099_base_exp.txt')
for line in f:
    (base, exp) = (int(i) for i in line.split(','))

    number = exp * log(base)

    if largestNumber < number:
        largestNumber = number
        result = lineNumber

    lineNumber += 1

f.close()
print ("Result:", result)
