#!/usr/bin/env python3

# Combinatoric selections
# Problem 53
#
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
# nCr = n!/(r!(n-r)!), where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

from math import factorial

result = 0

for n in range(1, 100+1):
    for k in range(1, n+1):
        if factorial(n)/factorial(k)/factorial(n-k) > 1000000:
            result += 1

print ("Result:", result)
