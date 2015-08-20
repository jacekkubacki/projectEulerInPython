#!/usr/bin/env python3

# Self powers
# Problem 48
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

print ("Result:", str(sum([pow(i, i) for i in range(1, 1000+1)]))[-10:])
