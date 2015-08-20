#!/usr/bin/env python3

# Ordered fractions
# Problem 71
#
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.


# http://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid.27s_algorithm
def gcd(a, b):
    while True:
        if a == b:
            return a
        elif a > b:
            a -= b
        elif a < b:
            b -= a


# 3/7 = 428571/999999, the fraction that is just a bit smaller is 428570/999999
# I'll check all denominators to make sure there are no other fractions between 428570/999999 and 3/7
resultNumerator = 428570
resultDenominator = 999999

for denominator in range(3, 1000000 + 1):
    # skip multiplies of 7 as 428570/999999 is the closest one to 3/7
    if denominator % 7 == 0:
        continue
    # find numerator for a given denominator, so the fraction is as close to as 3/7 as possible
    # numerator/denominator = 3/7 -> numerator = 3 * denominator / 7
    # numerator is an int, denominator is not divisible by 7 (see continue statement above),
    # so for numerator = int (3 * denominator / 7) we have numerator/denominator < 3/7 and (numerator + 1)/denominator > 3/7
    numerator = int(3 * denominator / 7.0)

    # check if numerator/denominator > resultNumerator/resultDenominator -> numerator * resultDenominator > resultNumerator * denominator
    if numerator * resultDenominator > resultNumerator * denominator:
        resultNumerator = numerator
        resultDenominator = denominator

# make sure resultNumerator/resultDenominator is a reduced proper fraction
divisor = gcd(resultNumerator, resultDenominator)
resultNumerator //= divisor
# don't need resultDenominator anymore
# resultDenominator //= divisor

print ("Result:", resultNumerator)
