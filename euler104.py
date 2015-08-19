#!/usr/bin/env python3
'''
Pandigital Fibonacci ends
Problem 104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order).
And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

from math import log10
import sys

a, b = 1, 1
aLow, bLow = 1, 1
index = 2

while True:
    # find next term (b)
    a, b = b, a + b
    # keep track of the last 9 digits
    aLow, bLow = bLow, (aLow + bLow) % 1000000000
    index += 1

    # check if bLow contains all the digits 1 to 9
    if len(set(list(str(bLow) + '0'))) == 10:
        # F2749 is the first term for which the first nine digits are 1-9 pandigital
        if index < 2749:
            continue

        # find order of magnitude
        m = int(log10(b))
        # find first nine digits of 'b'
        bHigh = b // (10 ** (m - 8))

        # check if bHigh contains all the digits 1 to 9
        if len(set(list(str(bHigh) + '0'))) == 10:
            print ("Result:", index)
            sys.exit()
