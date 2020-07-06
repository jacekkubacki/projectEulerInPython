#!/usr/bin/env python3

# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + ^22 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Solution:
# n-th sum of the squares is x(n) = 1^2 + 2^2 + ... + n^2
# n-th square of the sum is  y(n) = (1 + 2 + ... + n)^2
# We are looking for z(n) = y(n) - x(n)
#
# Let z(1) = 1^2 - 1^2 = 0
# What is z(n)?
# z(n) = y(n) - x(n) = ... = z(n-1) + 2*n*sum(1..n-1)

z = 0   # z(1)

for n in range(2, 100+1):  # z(2)..z(100)
    z += 2 * n * sum(range(1, n))

print("Result:", z)
