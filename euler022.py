#!/usr/local/bin/python3
'''
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string

# to use it in map()
# more readable than map(lambda s: s[1:-1], ...)
def dequote(s):
    return s[1:-1]
    
def namescore(s):
    alphabet = ['']
    alphabet += list (string.ascii_uppercase)
    name = list (s.upper())

    result = 0
    for letter in name: 
        result += alphabet.index(letter)

    return result

# with statement with file object: opens file in 'r' mode, closes file on exit
with open('names.txt') as f:
    data = f.read()

listOfNames = list(map(dequote, list(str(data).split(','))))
listOfNames.sort()

result = 0
for i in range (0, len(listOfNames)):
    result += (i + 1) * namescore(listOfNames[i])

print ("Result:", result)
