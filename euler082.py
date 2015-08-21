#!/usr/bin/env python3

# Path sum: three ways
# Problem 82
#
# NOTE: This problem is a more challenging version of Problem 81.
#
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
#
# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

# Solution:
# This time we will go through the matrix column by column.
# Column 0 - nothing to do
# Column 1 - for each element in the column:
#            - let's assume that the cheapest path is via the element on the left (same row, column - 1)
#            - check if any path going up/down and then one left is cheaper then the one above
#            - add the cheapest path to the temporary column
#          - add the cheapest paths to the current column and move to the next column
# Column 2 - repeat the algorithm for Column 1
# ...
# Column 79 (last one) - repeat the algorithm for Column 1 and then find the minimum value in the column

matrix = []
size = 80

f = open('p082_matrix.txt')
for line in f:
    matrix.append(list(map(int, line.split(','))))
f.close()

for column in range(1, size):

    tmp_column = [0 for x in range(0, size)]

    for row in range(0, size):
        # assume the cheapest way is via the element on the left
        min_path = matrix[row][column - 1]

        # check paths above
        # it is enough to check path that goes up and then turns one left
        r = row - 1  # start with the element immediately above the current element
        tmp = 0  # current weight
        while r >= 0:
            # accumulate the weight of the path
            tmp += matrix[r][column]
            if tmp > min_path:
                # too long already
                break
            if tmp + matrix[r][column - 1] < min_path:
                # new cheaper path found, save it
                min_path = tmp + matrix[r][column - 1]
            r -= 1

        # check paths below
        r = row + 1
        tmp = 0
        while r < size:
            tmp += matrix[r][column]
            if tmp > min_path:
                break
            if tmp + matrix[r][column - 1] < min_path:
                min_path = tmp + matrix[r][column - 1]
            r += 1

        # add the cheapest path to temporary column
        tmp_column[row] = min_path

    # update the column in matrix with the cheapest paths
    for i in range(0, size):
        matrix[i][column] += tmp_column[i]

print("Result:", min([x[size - 1] for x in matrix]))
