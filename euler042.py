#!/usr/bin/env python3

# Coded triangle numbers
# Problem 42
#
# The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from my_utils import dequote, word_value

with open('p042_words.txt') as f:
    data = f.read()

triangleNumbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

listOfWords = list(map(dequote, data.split(',')))

result = 0
for word in listOfWords:
    value = word_value(word)

    while value > triangleNumbers[-1]:
        # we need more tringle numbers in 'triangleNumbers'
        n = len(triangleNumbers)
        triangleNumbers.append(n*(n+1)//2)

    if value in triangleNumbers:
        result += 1

print ("Result:", result)
