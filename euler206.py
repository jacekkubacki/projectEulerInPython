#!/usr/local/bin/python3
'''
Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
'''
'''
Solution:

Let b = 1_2_3_4_5_6_7_8_9_0 and a^2 = b, we are looking for 'a'.
'a' must be in range (1,010,101,010.1010101010 < sqrt(min(1_2_3_4_5_6_7_8_9_0)) < sqrt(max(1_2_3_4_5_6_7_8_9_0)) <  1,389,244,398.9449804
Also, 1_2_3_4_5_6_7_8_9_0 must end with 900 ('a' must have 0 at the end, so a^2 has two 0s), so 'a' must end with either 30 or 70.

Personally I prefer the solution with regular expression, but it is slower...

import re

pattern = re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d900")


def add30and70(x, y):
    for i in range(x, y, 100):
        yield i + 30
        yield i + 70

for a in add30and70(1010101000, 1389244398):
    if pattern.match(str(a * a)):
        print ("Result:", a)
        break
'''


def add30and70(x, y):
    for i in range(x, y, 100):
        yield i + 30
        yield i + 70


for a in add30and70(1010101000, 1389244398):
    b = str(a * a)
    # check if b has the correct digits in the correct place
    if   b[14] != '8':
        continue
    elif b[12] != '7':
        continue
    elif b[10] != '6':
        continue
    elif  b[8] != '5':
        continue
    elif  b[6] != '4':
        continue
    elif  b[4] != '3':
        continue
    elif  b[2] != '2':
        continue
    # n[0] is guaranteed to be '1'
    else:
        # b is of the form 1_2_3_4_5_6_7_8_9_0
        print ("Result:", a)
        break
