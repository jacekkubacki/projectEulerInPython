#!/usr/local/bin/python3
'''
Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''
'''
Solution:

Notice that:
a1 = 1 + 1/2
a2 = 1 + 1/(1 + a1)
a3 = 1 + 1/(1 + a2)
etc

Let an = n/d, then an+1 = 1 + 1(1 + an) = 1 + 1/(1 + n/d) = 1 + 1/(d/d + n/d) = 1 + 1/((n + d)/d) = 1 + d/(n + d) =
   = (n + d)/(n + d) + d/(n + d) = (n + d + d)/(n + d)
'''

from math import log10

result = 0

n = 3
d = 2

i = 2
while i < 1000:
    # it would be more readable with temp variable: tmp = d, d += n, n += 2*tmp
    # but it can also be done without it: d -> n + d
    d += n
    # n -> n + d + d, but d has already been updated and equals to n + d, so n = 2 * d - n
    n = 2 * d - n
    # clever check if n has more digits than d without converting n and s to strings
    if int(log10(n)) > int(log10(d)):
        result += 1
    i += 1

print ("Result:", result)
