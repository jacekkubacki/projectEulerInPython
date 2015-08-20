#!/usr/bin/env python3

# Dice Game
# Problem 205
#
# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins.
# The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin?
# Give your answer rounded to seven decimal places in the form 0.abcdefg

from itertools import product

# lists initialised with 0
Pete9D4  = [0 for i in range (0, 9 * 4 + 1)]
Colin6D6 = [0 for i in range (0, 6 * 6 + 1)]

# count cases favorable for each sum
for case in product([1, 2, 3, 4], repeat=9):
    Pete9D4[sum(case)] += 1
for case in product([1, 2, 3, 4, 5, 6], repeat=6):
    Colin6D6[sum(case)] += 1

casesFavorable = 0 # Pyramidal Pete beats Cubic Colin
allCases = pow(4, 9) * pow(6, 6) # = len(Pete9D4) + len (Colin6D6)

for index, s in enumerate(Pete9D4):
    # for each given sum 's'
    # multiply Pete's cases by the sum of all the Colin cases for which Pete wins
    casesFavorable += s * sum(Colin6D6[:index])

print ("Result:", round(casesFavorable / allCases, 7))
