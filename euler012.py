#!/usr/bin/env python3
'''
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

'''
Solution:

The number of divisors of a given number can be easily calculated:
http://www.manhattangmat.com/forums/is-there-a-formula-to-calculate-the-number-of-factors-t2500.html
Suppose your number factors as a product p^a * q^b * .... *r^k.
Then to get any factor you want you should take up to a copies of p, up to b copies of q, etc. and multiply them all together.
The number of ways you can choose up to a copies of p is (a+1) since you could choose 0 copies, 1 copy, 2 copies, ..., a copies.
Likewise there are (b+1) ways to choose how many q's to include, etc.
So the number of factors for your number would be (a+1)*(b+1)*...(k+1).
'''

from myUtils import primeFactors
from collections import Counter

triangleNumber = 1
naturalNumber  = 2

while True:
    triangleNumber += naturalNumber

    numberOfFactors = 1
    for exp in Counter(primeFactors(triangleNumber)).values():
        numberOfFactors *= (exp + 1)

    if numberOfFactors > 500:
        print ("Result:", triangleNumber)
        break

    naturalNumber += 1
