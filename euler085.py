#!/usr/bin/env python3

# Counting rectangles
# Problem 85
#
# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.
#
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

# Solution:
# For the 3x2 grid we have:
#  6 = 3 * 2  1x1 squares
#  3 = 3 * 1  1x2 rectangles
#  4 = 2 * 2  2x1 rectangles
#  2 = 2 * 1  2x2 squares
#  2 = 1 * 2  3x1 rectangles
#  1 = 1 * 1  3x2 rectangle
#
# 18 = 6 + 3 + 4 + 2 + 2 + 1 = (3 * 2)+(3 * 1) + (2 * 2)+(2 * 1) + (1 * 2)+(1 * 1) = 3*(2 + 1) + 2(2 + 1) + 1*(2 + 1) =
#    = (3 + 2 + 1) * (2 + 1) = (1 + 2 + 3) * (1 + 2)
# Looks like the formula to find the number of rectangles in n x m grid is (1 + 2 + 3 + ... + n) * (1 + 2 + 3 + ... + m)
#
# Each factor is a sum of arithmetic progression where a1 = 1 and d = 1,
# Sn = n * (2 * a1 + (n - 1) * d) / 2 = n * ( 2 * 1 + (n - 1) * 1) / 2 = n * (2 + n - 1) / 2 = n * (n + 1) / 2
# Sm = m * (m + 1) / 2
#
# We are looking for a grid with 2000000 rectangles, so
# Sn * Sm = 2000000 => (n * (n + 1) / 2) * (m * (m + 1) / 2) = 2000000 => n * (n + 1) * m * (m + 1) = 8000000
#
# Assuming that n <= m, then the maximum value for n is when n = m (the bigger m is the smaller n gets), so
# m * (m + 1) * m * (m + 1) = 8000000 => m^2 * (m + 1)^2 - 8000000 = 0 => ... => m1 ~ -53.685, m2 ~ 52.685
# so it is enough to check grids for n = 1, 2, 3, ..., 53
#
# If n is known, then we have n * (n + 1) * m * (m + 1) = 8000000 => m^2 + m - 8000000/(n^2 + n) = 0
# We can solve this quadratic equation and for each positive root find floor (fm) and ceiling (cm)
# and then check how close n * (n + 1) * cm * (cm + 1) and n * (n + 1) * cf (cf + 1) are to 8000000

from math import ceil, floor, sqrt

# one of the possible solutions we have already found is when n = m ~ 52.685, ceil(n) = 53, so
grid_area = 53 * 53
nearest_solution = abs(8000000 - 53**4)  # how close the current solution is from 8000000

for n in range (1, 53 + 1):
    # m^2 + m - 8000000/(n^2 + n) = 0 => a = 1, b = 1, c = 8000000/(n^2 + n)
    delta = 1 + 32000000 / (n * n + n)
    # m1 = (-b - sqrt(delta)) / (2a) will always be negative because b = 1 and c is a large positive number
    # so we can focus on m2 only
    m2 = (-1 + sqrt(delta)) / 2
    fm = int(floor(m2))
    cm = int(ceil(m2))

    for m in [fm, cm]:
        diff = abs(8000000 - (n * n + n) * (m * m + m))
        if diff < nearest_solution:
            nearest_solution = diff
            grid_area = n * m

print("Result:", grid_area)
