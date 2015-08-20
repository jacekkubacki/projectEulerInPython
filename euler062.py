#!/usr/bin/env python3

# Cubic permutations
# Problem 62
#
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import Counter

# Counter will keep track of cubes that can be permuted
c = Counter()
# dictionary will keep track of the smallest cube for set of permutations
d = {}

# let's start with 5, as 5^3 is the first cube with 3 digits -> more than 5 permutations
n = 5

while True:
    n3 = n ** 3

    # sort the digits, all permutations will contain the same digits
    s = ''.join(sorted(str(n3)))
    # use the sorted string to count permutations
    c.update([s])

    # add 's' to dictionary if it is the first occurrence
    # 'n3' is the smallest cube that uses all the digits from string 's'
    d[s] = d.setdefault(s, n3)

    # get the most common string 'perm' in Counter 'c'
    perm, count = c.most_common(1)[0]

    if count == 5:
        # the smallest cube is in dictionary 'd'
        print ("Result:", d[perm])
        break

    n += 1
