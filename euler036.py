#!/usr/bin/env python3

# Double-base palindromes
# Problem 36
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

result = 0

# We skip even numbers as they end with '0' in base 2
# and as a consequence are not palindromic
for p in range (1, 1000000, 2):
    # Is it a decimal palindrome?
    if str(p) == str(p)[::-1]:
        # Is it a binary palindrome?
        if bin(p)[2:] == bin(p)[:1:-1]:
            result += p

print ("Result:", result)
