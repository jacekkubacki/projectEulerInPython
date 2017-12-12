#!/usr/bin/env python3

# Spiral primes
# Problem 58
#
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

from my_utils import is_prime

numbersOnDiagonals = 1  # '1' is on both diagonals
numberOfPrimes = 0      # no prime numbers yet

currentNumber = 1
step = 2

while True:
    # check numbers on three diagonals
    for i in range(0, 3):
        currentNumber += step
        if is_prime(currentNumber):
            numberOfPrimes += 1
    # skip right bottom diagonal
    currentNumber += step

    numbersOnDiagonals += 4
    # check ratio, float() used to make sure code works correctly with Python 2.x
    if numberOfPrimes / float(numbersOnDiagonals) < 0.1:
        # side length = step + 1
        print ("Result:", step + 1)
        break

    # next layer
    step += 2
