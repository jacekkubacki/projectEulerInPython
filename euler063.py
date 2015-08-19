#!/usr/bin/env python3
'''
Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

'''
Solution:

Raise each integer number (starting with 1) to consecutive powers (starting with 1).
Notice that there is no need to check numbers >= 10 as the number of digits is always bigger than the exponent.
Also, notice that every single-digit number is a 1st power of itself.

For a given number (from 1 to 9) we will check the consecutive powers  (starting with 1)
till the number of digits is different (lower) than the exponent,
because it will be lower for all the exponents bigger than the current one.
'''

result = 0

for number in range (1,10):
    exponent = 1
    while len(str(number**exponent)) == exponent:
        result += 1
        exponent += 1
    
print ("Result:", result)
