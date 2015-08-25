#!/usr/bin/env python3

# Counting summations
# Problem 76
#
# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?


class CountingSummations:

    different_ways = 0
    lookup_summations = {}  # store summations to save time when running recursive function

    def __init__(self, total):
        self.total = total
        self.different_ways = self.count_the_ways(0, self.total - 1)

    def count_the_ways(self, current_sum, last_integer):
        """Counts the number of different ways _total_ can be written as a sum of integers <= last_integer"""
        try:
            # get the value from lookup dictionary to save time
            return self.lookup_summations[(current_sum, last_integer)]
        except KeyError:
            # the value is not in the lookup dictionary, let's calculate it
            result = 0

            # too much, not a valid sum
            if current_sum > self.total:
                return 0

            # valid combination found
            if current_sum == self.total:
                return 1

            # if the last integer is 1, then all remaining addends are 1
            if last_integer == 1:
                return 1

            # try to add every possible integer that is not greater than the last one
            for i in range(last_integer, 0, -1):
                result += self.count_the_ways(current_sum + i, i)

            # add the result to lookup dictionary, so next time the value can be retrieved instead of calculated
            self.lookup_summations[(current_sum, last_integer)] = result

            return result

if __name__ == '__main__':
    print("Result:", CountingSummations(100).different_ways)
