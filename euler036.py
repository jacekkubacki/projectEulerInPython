#!/usr/local/bin/python3
'''
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def dec2bin (i):
    return bin(i)[2:]

palindromes=[]
# Build the list of decimal palindromes.
# We skip even numbers as they end with '0' in base 2
# and as a consequence are not palindromic
for p in range (1, 1000000,2):
    l = list (str(p))
    r = list (l)
    r.reverse()
    if l == r:
        palindromes.append(p)

doubleBasedPalindromes = []
# Parse the list of decimal palindromes and build the list of binary palindromes 
# The numbers in the list will be both decimal and binary palindromes
for p in palindromes:
    l = list (dec2bin(p))
    r = list (l)
    r.reverse()
    if l == r:
        doubleBasedPalindromes.append(p)

print ("Result:", sum(doubleBasedPalindromes))
