#!/usr/bin/env python3

# Digit fifth powers
# Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Solution:
# Brute force :)
# All 1-, 2-, 3-, 4- and 5-digits numbers should be checked, as 9^5 = 59049.
# For 6-digits numbers the maximum sum is 6*9^5 = 354294, so there is no need to check numbers bigger than that.
# (we can even analyze a bit further and note that as a consequence there is no need to check numbers bigger than 3^5 + 5*9^5 and so on...)

fifthPowers = [pow(i, 5) for i in range(0, 10)]

result = 0
for number in range(2, 6*fifthPowers[9]):
    s = 0
    n = number
    while n > 0:
        s += fifthPowers[n % 10]
        n //= 10
    if s == number:
        result += number
    
print ("Result:", result)
