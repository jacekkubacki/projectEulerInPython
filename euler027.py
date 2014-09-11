#!/usr/local/bin/python3
'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.

The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
'''
Solution:

Let f(n) = n^2 + a*n + b.
For a = 1 and b = 41 f(n) produces 40 primes for the consecutive values n = 0 to 39.

f(0) = b, so to find coefficients that produce >= 40 primes b must be prime.

If b is even then b must be 2 (b is prime).
f(2) = 2^2 + 2*a + b = 6 + 2a is even, so must equal 2 in order to be prime -> 6 + 2a = 2 -> a = -2.
But f(4) = 4^2 + 4*a + b = 16 - 8 + 2 = 6 - not prime.
So to find coefficients that produce >= 40 primes b must be prime and odd.

f(1) = 1 + a + b, f(1) must be prime, so either f(1) = 2 or f(1) is odd.
If f(1) = 2 -> 1 + a + b = 2 -> b = 1 - a
f(3) = 3^3 + 3*a + b = 9 + 3*a + (1 - a) = 10 + 2*a - is even, so must equal 2 (to be prime) -> 10 + 2*a = 2 -> a = -4
But f(5) = 5^2 + 5*a + b = 25 - 20 + 5 = 10 - not prime.
So to find coefficients that produce >= 40 primes f(1) must be odd -> 1 + a + b must be odd and b is odd -> a must be odd.

f(1) = 1 + a + b, but f(1) must be prime and odd, so 1 + a + b >= 3 (lowest odd prime) -> b >= 2 - a

To summarise: in order to find coefficients, a and b, for the quadratic expression n^2 + an + b
that produces 40 or more primes for consecutive values of n, starting with n = 0:
* a must be odd
* b must be prime > 2
* b >= 2 - a
'''

from myUtils import isPrime, listOfPrimes
from bisect import bisect_left

# for a = 1 < 1000 and b = 41 < 1000 the quadratic expression n^2 + n + 41 returns 40 primes for the consecutive values n = 0 to 39
maxConsecutivePrimes = 40
result = 1 * 41

# b is prime > 2
primes = listOfPrimes(1000)[1:]

# a must be odd
for a in range (-999, 1000, 2):

    # bisect_left locate the insertion point to maintain sorted order
    # we will use it to find the index of a first element >= 2 - a in prime list to make sure that b >= 2 - a
    for b in primes[bisect_left(primes, 2 - a):]:

        # f(0) = b, b is guaranteed to be prime
        # let's start from n = 1
        n = 1
        consecutivePrimes = 1

        while True:
            if isPrime (n * n + a * n + b):
                consecutivePrimes += 1
            else:
                break
            n += 1

        if maxConsecutivePrimes < consecutivePrimes:
            maxConsecutivePrimes = consecutivePrimes
            result = a * b

print ("Result:", result)
