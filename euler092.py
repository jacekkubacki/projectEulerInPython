#!/usr/bin/env python3

# Square digit chains
# Problem 92
#
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

import itertools

class SquareDigitChains89:
    """Finds how many starting numbers below 10^power will arrive at 89?"""

    lookup_squares = [x ** 2 for x in range(0, 10)]
    lookup_arrivals = {0: 0, 1: 1, 89: 89}  # 0 added to simplify the usage of itertools.product
    result = 0

    def __init__(self, power):
        self.length = power  # this is maximum number of digits in the starting number

        # add values to lookup dictionary
        # it can be optimized by building number chain and adding the same arrival value for each element of the chain
        # current version is fast enough and more readable
        maximum_sum = self.length * (9 ** 2)
        for number in range(1, maximum_sum + 1):
            current = number
            while True:
                try:
                    # if _current_ is in dictionary, then _number_ will arrive at the same value
                    self.lookup_arrivals[number] = self.lookup_arrivals[current]
                    break  # while

                except KeyError:
                    # find the next number in the chain
                    current = self.square_digits(current)

        # find the answer
        self.result = self.count_89_chains()

    def square_digits(self, number):
        """Calculates the square of the digits in _number_"""
        result = 0
        while number > 0:
            # using lookup table to speed up this function
            result += self.lookup_squares[number % 10]
            number //= 10
        return result

    def count_89_chains(self):
        """Counts how many numbers arrive at 89"""
        result = 0
        for starting_number in itertools.product(self.lookup_squares, repeat=self.length):
            # starting_number is a list of integers
            # instead of using digits 0-9 to represent each starting number we use lookup_squares
            # so after adding them up we just check in lookup_arrivals if the starting_number arrives at 89
            if self.lookup_arrivals[sum(starting_number)] == 89:
                result += 1
        return result

print("Result:", SquareDigitChains89(7).result)
