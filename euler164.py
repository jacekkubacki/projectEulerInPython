#!/usr/bin/env python3

# Numbers for which no three consecutive digits have a sum greater than a given value
# Problem 164
#
# How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?

# the key in the dictionary represents the last three digits of a current number
# the value represent the quantity of such numbers
# e.g. lookup[(1, 2, 3)] = 4 means that there are 4 n-digit numbers ending with 123
lookup = {}

# find all valid 3 digit numbers that exhibit the property we are looking for
# starting from 1 to form a valid 3-digit number
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if a + b + c <= 9:
                # there is only one 3 digit number with that property
                lookup[(a, b, c)] = 1

# iterate and update the lookup dictionary for 4-, 5-, ..., 20-digit numbers
for length in range(4, 20 + 1):
    # this is temporary dictionary that will replace current lookup dictionary at the end of the iteration
    new_lookup = {}

    # iterate through all 'numbers' in lookup dictionary
    for suffix in lookup.keys():
        # create new_suffix based on suffix and make sure sum(new_suffix) <= 9
        for i in range(0, 9 - suffix[1] - suffix[2] + 1):
            new_suffix = (suffix[1], suffix[2], i)
            try:
                # add the current quantity to the quantity of the numbers with new_suffix in the new_lookup dictionary
                new_lookup[new_suffix] += lookup[suffix]
            except KeyError:
                # the key doesn't exist - create one
                new_lookup[new_suffix] = lookup[suffix]
    # new_lookup dictionary contains updated values, let's update lookup dictionary for the next iteration
    lookup = new_lookup.copy()

print ("Result:", sum(lookup.values()))
