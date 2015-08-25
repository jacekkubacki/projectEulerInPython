#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coin sums
# Problem 31
#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

COINS = [200, 100, 50, 20, 10, 5, 2, 1]
TOTAL = 200


def addCoins(currentSum, lastCoin):
    """Add COINS in a descending value order and return the number of different ways currentSum can be obtained"""
    # This is a recursive function without any optimization, see Problem 76 for more optimal solution
    
    result = 0

    # too much, not a valid combination
    if currentSum > TOTAL:
        return 0

    # valid combination found
    if currentSum == TOTAL:
        return 1

    # if the last digit is 1, then all remaining coins are 1p
    if lastCoin == 1:
        return 1

    # add a new coin if the value is smaller or equal to the last one
    for c in COINS:
        if c <= lastCoin:
            result += addCoins(currentSum + c, c)

    return result

# lastCoin in addCoins is 200, so all COINS can be used in the first step
print ("Result:", addCoins(0, 200))
