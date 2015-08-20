#!/usr/bin/env python3

# Path sum: two ways
# Problem 81
#
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

# Solution:
# Walk through the matrix from upper left to bottom right corner, selecting 'cheaper' route where possible and adding the weights on the fly
# 1. start at (0,0)
# 2. we can go either to (0,1) or to (1,0), add value of (0,0) to both (0,1) and (1,0)
# 3. third 'diagonal' - only one way to get to (0,2) and (2,0)
#    two ways to get for (1,1), compare the weights and select cheaper one (in this case (0,1))
# etc.

matrix = []
size = 80

f = open('p081_matrix.txt')
for line in f:
    matrix.append(list(map(int, line.split(','))))
f.close()

# start with the second 'diagonal'
for diagonal in range(1, 2 * size - 1):
    # start from left (x == 0)
    x = 0
    y = diagonal

    while y >= 0:
        # make sure that x and y are valid coordinates for large values of diagonal
        if x < size and y < size:
            if x == 0:
                # this is an edge element with only one way of getting to
                matrix[x][y] += matrix[x][y-1]
            elif y == 0:
                # this is an edge element with only one way of getting to
                matrix[x][y] += matrix[x-1][y]
            else:
                # select the cheaper route
                matrix[x][y] += min(matrix[x][y-1], matrix[x-1][y])

        # select the next point on the diagonal (one up and right)
        x += 1
        y -= 1

print ("Result:", matrix[size - 1][size - 1])
