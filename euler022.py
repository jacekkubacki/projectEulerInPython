#!/usr/bin/env python3

# Names scores
# Problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

from my_utils import dequote, word_value

with open('p022_names.txt') as f:
    data = f.read()

list_of_names = list(map(dequote, data.split(',')))
list_of_names.sort()

result = 0
for i in range(0, len(list_of_names)):
    result += (i + 1) * word_value(list_of_names[i])

print("Result:", result)
