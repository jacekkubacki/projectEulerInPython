#!/usr/bin/env python3

# Champernowne's constant
# Problem 40
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000


def findDigit(indexInSet, numberOfDigits):
    # special case for the first nine digits
    if indexInSet < 10 and numberOfDigits == 1:
        return indexInSet

    # calculate number of digits in all numberOfDigits long numbers
    lengthOfCurrentSet = numberOfDigits * 9 * (10 ** (numberOfDigits - 1))

    if indexInSet <= lengthOfCurrentSet:
        # the digit we are looking for is in current set
        # this set starts with:
        startNumber = 10 ** (numberOfDigits - 1)
        # what is the offset?
        offset = (indexInSet - 1) // numberOfDigits

        # the digit we are looking for is in 'number'
        number = startNumber + offset
        # find the index of the digit
        indexInNumber = (indexInSet - 1) % numberOfDigits

        return int(str(number)[indexInNumber])

    else:
        # the digit is not in current set, check the set of all numbers that are 1 digit longer
        return findDigit(indexInSet - lengthOfCurrentSet, numberOfDigits + 1)

result = 1
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    result *= findDigit(n, 1)

print ("Result:", result)
