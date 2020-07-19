#!/usr/bin/env python3

# Reciprocal cycles
# Problem 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def unit_fraction(denominator):
    """ Return length of recurring cycle """
    # assumption: denominator > 1
    dividend, divisor = 1, denominator
    # list of (quotient, reminder)
    quotient_reminder = []

    while True:
        dividend *= 10
        quotient, reminder = dividend // divisor, dividend % divisor

        if reminder == 0:
            # no recurring cycle
            return 0
        if (quotient, reminder) in quotient_reminder:
            # recurring cycle found, current index is len(quotient_reminder)
            return len(quotient_reminder) - quotient_reminder.index((quotient, reminder))
        else:
            quotient_reminder.append((quotient, reminder))

        # new dividend for next iteration
        dividend = reminder

# 1/7	= 	0.(142857)
denominator = 7
cycle_length = 6

for d in range(999, denominator, -1):
    if unit_fraction(d) > cycle_length:
        denominator = d
        cycle_length = unit_fraction(d)

print("Result:", denominator)
