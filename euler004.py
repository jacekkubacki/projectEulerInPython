#!/usr/local/bin/python3
'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindrome = 0
limit = 100 # the smallest 3-digit number

# starting with the big numbers
for x in range (999, limit, -1):
    # x will be always >= y
    for y in range (x, limit, -1):
        p = x * y
        # check if p is the same as reversed p
        if str(p) == str(p)[::-1]:
            if palindrome < p:
                palindrome = p
                # there is no need to check numbers lower than y
		# as the product is guaranteed to be smaller than x*y
                limit = y 
                # the palindrome cannot be bigger for a given x
                break
                
print ("Result:", palindrome)
    
