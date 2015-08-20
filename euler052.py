#!/usr/bin/env python3

# Permuted multiples
# Problem 52
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import sys

oom = 10  # order of magnitude

while True:
    # It is enough to check only the numbers with the same amount of digits
    # e.g.: when we start with number == 100
    # then there is no need to check numbers > 1000 / 6
    # as we want 6*number to have the same amount of digits as 'number'

    number = oom 
    
    while number < oom*10/6:

        # to compare other sets with
        set2x = set(str(2 * number))

        solution = True
        for m in [3, 4, 5, 6]:
            # compare 2x with 3x, 4x, 5x and 6x
            if set2x != set(str(m * number)):
                solution = False
                break

        if solution == True:
            print ("Result:", number)
            sys.exit(0) 

        number += 1

    oom *= 10  # next oom
