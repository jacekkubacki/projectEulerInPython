#!/usr/bin/env python3

# Triangle containment
# Problem 102
#
# Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, such that a triangle is formed.
#
# Consider the following two triangles:
#
# A(-340,495), B(-153,-910), C(835,-947)
#
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
#
# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the triangles in the example given above.

# Solution:
# The linear equation of a line passing through two points (x1,y1) and (x2,y2) is:
# (x2 - x1)*(y - y1) = (y2 - y1)*(x - x1) => (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1) = 0
#
# Let f(x, y) = (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1).
# f(x, y) = 0 only if (x,y) lies on the line.
# If it doesn't, then f(x,y) is either positive or negative depending on which side of the line (x,y) lies.
# Notice that (0,0) is inside the triangle ABC if:
# 1. A and (0,0) lie on the same side of the line passing through B and C
# 2. B and (0,0) lie on the same side of the line passing through A and C
# 3. C and (0,0) lie on the same side of the line passing through A and B

def sign(x):
    """Returns sign of x"""
    return (x > 0) - (x < 0)


def line(x1, y1, x2, y2, x, y):
    """Substitutes x and y in the linear equation of a line that passes through two points: (x1,y1) and (x2,y2)"""
    return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)


result = 0
with open('p102_triangles.txt') as f:
    for row in f:
        ax, ay, bx, by, cx, cy = tuple(map(float, row.split(',')))
        if sign(line(bx, by, cx, cy, ax, ay)) == sign(line(bx, by, cx, cy, 0, 0)) and\
           sign(line(ax, ay, cx, cy, bx, by)) == sign(line(ax, ay, cx, cy, 0, 0)) and\
           sign(line(ax, ay, bx, by, cx, cy)) == sign(line(ax, ay, bx, by, 0, 0)):
            result += 1

print("Result:", result)
