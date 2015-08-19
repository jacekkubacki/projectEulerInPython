#!/usr/bin/env python3
'''
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

'''
Solution:
The non-trivial examples are of a form ax/xb or xa/bx, where x is the digit to be cancelled.
We are looking for a, x and b (all single digit numbers) that solve following equations
ax/xb = a/b => (10*a + x)*b = (10*x + b)*a
or
xa/bx = a/b => (10*x + a)*b = (10*b + x)*a
'''

from collections import Counter
from functools import reduce
from myUtils import primeFactors

numerator = 1
denominator = 1

# ax/bx
for a in range (1, 10):
    # x <= a otherwise the fraction will not be < 1
    # also, if x == a, then we will end up with a trivial fraction
    # so x >= a + 1
    for x in range (a + 1, 10):
        # b > 0 to make sure that after cancelling x the denominator is a non-zero number
        for b in range (1, 10):
            if (10 * a + x) * b == (10 * x + b) * a:
                numerator *= a
                denominator *= b

# xa/bx
for x in range (1, 10):
    # a > 0 to make sure that after cancelling x the numerator is a non-zero number
    for a in range (1, 10):
        #  b >= x + 1, so the fraction is < 1
        for b in range (x + 1, 10):
            if (10 * a + x) * b == (10 * x + b) * a:
                numerator *= a
                denominator *= b

# reduce fraction by looking at the prime Factors
n = Counter(primeFactors(numerator))
d = Counter(primeFactors(denominator))
reducedDenominator = list((d - n).elements())
# multiply all remaining factors in denominator
print ("Result:", reduce(lambda a, b: a * b, reducedDenominator))
