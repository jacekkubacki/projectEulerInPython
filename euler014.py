#!/usr/bin/env python3

# Longest Collatz sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


# seqLength will contain the length of Collatz sequence for all numbers < 1000000
seqLength = [0, 1]

# check every number < 1000000 starting with 2
for number in range (2, 1000000):
    steps = 0
    current = number

    while True:
        steps += 1
        if current % 2 == 0:
            # apply the rule for even numbers
            current //= 2
            if current < number:
                # the length of the sequence has already been calculated
                seqLength.append(seqLength[current] + steps)
                break
        else:
            # apply the rule for odd numbers
            current = 3 * current + 1

print ("Result:", seqLength.index(max(seqLength)))
