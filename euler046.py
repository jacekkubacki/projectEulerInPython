#!/usr/bin/env python3

# Goldbach's other conjecture
# Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from my_utils import is_prime

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
double_squares = [2, 8, 18, 32]

number = 33
while True:
    number += 2

    # add another twice a square to the list
    if double_squares[-1] < number:
        double_squares.append(2*(len(double_squares) + 1)**2)

    # if it is a prime number then add it to the list
    if is_prime(number):
        primes.append(number)
        continue
    else:
        # this is a composite number
        conjecture = False  # assume the conjecture to be false
        # check if the difference between _number_ and any element of _double_square_ is a prime number
        for ds in double_squares:
            if (number - ds) in primes:
                # odd composite number can be written as the sum of a prime and twice a square, so...
                conjecture = True
                break
        # exit while loop if the conjecture is False
        if not conjecture:
            break

print("Result:", number)
