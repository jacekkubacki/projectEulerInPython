#!/usr/local/bin/python3
'''
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

'''
Solution:

The identity contains 9 digits only when multiplicand is 1- or 2-digits number, assuming that multiplicand < multiplier.
When multiplicand is a 1-digit number then multiplier must be a 4-digits number,
When multiplicand is a 2-digit number then multiplier must be a 3 digits number.
'''

from itertools import permutations

results = []

# multiplicand should (1) be greater than 1 (2) not be multiple of 10 or 11
# otherwise the identity will not be pandigital, e.g. 10 x 234 = 2340
for multiplicand in [m for m in range(2,100) if m % 10 and m % 11]:
    multiplicandString = str(multiplicand)
    # only digits that are not in multiplicand
    
    digits = [str(i) for i in range (1,10) if str(i) not in multiplicandString] 
    # create 3- or 4-digits multipliers
    for multiplierString in [''.join(p) for p in permutations(''.join(digits), 4 if multiplicand < 10 else 3)]:
        multiplier = int(multiplierString)
        product = multiplicand * multiplier
        identity = multiplicandString + multiplierString + str(product)
        
        # to rule out 10-digits identities, e.g.: 7 x 4321 = 30247
        if len(identity) != 9: 
            break
        
        # '0' added to rule out identities with products containing '0'
        # e.g.: 2 x 1548 = 3096 consists of 9 different digits, but is not 1 to 9 pandigital
        if len(set('0' + identity)) == 10: 
            if product not in results: 
                results.append(product)

print ("Result:", sum(results))
    