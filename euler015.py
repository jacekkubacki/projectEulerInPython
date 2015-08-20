#!/usr/bin/env python3

# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?

# Solution:
# Every route will contain 20 'downs' and 20 'rights'.
# There 40! possible ways of arranging 40 elements, but we can't distinguish one 'down' from the other.
# There 20! possible ways of arranging 'downs' that will give us the same route, same for 'rights'.
# So the answer is 40!/(20!*20!).

from math import factorial
print ("Result:", factorial(40)//pow(factorial(20), 2))

