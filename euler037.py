#!/usr/bin/env python3

# Truncatable primes
# Problem 37
#
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from itertools import product

from my_utils import is_prime


class ContinueLoop(Exception):
    pass


class StopExecution(Exception):
    pass


def get_all_numbers():
    middle_digits = [1, 2, 3, 5, 7, 9]
    number_of_digits = 2
    while True:
        for i in product(middle_digits, repeat=number_of_digits):
            yield i
        number_of_digits += 1


def remove_digits(number):
    number_of_digits = len(number)
    for i in range(number_of_digits - 1, 0, -1):
        yield number[:i]  # remove digit(s) from right
        yield number[-i:]  # remove digit(s) from left


def calculate_value(number):
    number_of_digits = len(number)
    value = 0
    for i in range(number_of_digits):
        digit = number[i]
        value = value * 10 + digit
    return value


number_of_primes = 0
threshold = 11
result = 0

for x in get_all_numbers():
    try:
        value = calculate_value(x)

        if is_prime(value) is False:
            raise ContinueLoop

        for z in remove_digits(x):
            zz = calculate_value(z)
            if is_prime(zz) is False:
                raise ContinueLoop

        number_of_primes += 1
        result += value
        if number_of_primes == 11:
            raise StopExecution

    except ContinueLoop:
        continue
    except StopExecution:
        break


print(f"Result: {result}")
