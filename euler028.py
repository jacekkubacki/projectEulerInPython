#!/usr/local/bin/python3

'''
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

'''
Solution:
The numbers on the diagonals are the vertices of the squares we build around '1' when drawing a spiral.
We start with number 1.
Then every second number is a vertex of a 3x3 square around '1'.
Then every fourth number is a vertex of a 5x5 square around the 3x3 square.
Then every sixth  number...
'''

number = 1
step = 2

result = number

while number < 1001 * 1001:
    for i in range (0,4):
        number += step
        result += number
    step += 2

print ("Result:", result)