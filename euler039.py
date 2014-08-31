#!/usr/local/bin/python3
'''
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

'''
Solution:
For a given p:
1) Let c be the hypotenuse, the longest side of the right-angled triangle.
- it cannot be shorter than p//3 to be the longest side
- it cannot be longer  than p//2 to make sure a, b and can form a triangle (c < a + b)
2) Let b be the longer cathetus
- it cannot be shorter than (p - c) // 2 to be longer than a
- it cannot be longer than c
3) Let a be the shorter cathetus
- a = p - b - c
'''

# numberOfSolutions[p] will return the number of solutions for a given p
numberOfSolutions = [0 for i in range (0, 1000 + 1)]

for p in range (3, 1000 + 1):
    for c in range (p//3, p//2): 
        for b in range ((p-c)//2, c):
            a = p - c - b # check if a > 0 removed as _a_it is always positive
            if c * c == a * a + b * b:
                numberOfSolutions[p] += 1

print ("Result:", numberOfSolutions.index(max(numberOfSolutions)))
