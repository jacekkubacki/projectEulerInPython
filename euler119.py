#!/usr/bin/env python3
'''
Digit power sum
Problem 119

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512.
Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

'''
Solution:
The value of each element of 'powers' list will be some power of its index, except 0,1,2.
We can skip
0 - because the sum of digits of a positive number is always > 0
1 - because for every two-digits number x with sum of its digits = 1
    we have x != 1^n = 1 for every positive integer n
2 - because for every power of two with at least two digits the sum of digits is always > 2
    (possible units values are 2,4,8,6 + at least one non-zero digit)

The plan is to check only the elements of the list.

The algorithm is:
- start with 1-digit numbers in the list, powers[index] = index^1 = index
* find the smallest number in the list (already some power of some index)
- check if sum of the digits for that number is the same as the index of the number in the list
  if so then add the number found to 'a' list, but ignore 1-digit numbers
- replace the current number (index^n) with the next power (index^(n+1))
- make sure the list contains an entry for every possible sum of digits,
  the maximum sum of digits for n-digits number is n*9
- go to (*) and repeat until 30th term has been found
'''

from myUtils import sumOfDigits

powers = [0,1,2,3,4,5,6,7,8,9]
a = []

# find 30 terms
while len(a) < 30:

    # find the smallest number in the list and its index, ignore powers of 0,1,2
    number = min (powers[3:])
    index  = powers.index(number)
    
    if sumOfDigits(number) == index:
        if len(str(number)) == 1:
            pass # ignore 1-digit numbers
        else:
            # next term has been found, add it to 'a'
            a.append(number)

    # replace the current value in the list with the next power (multiply the existing value by index) 
    powers[index] *= index

    # add more elements to the list if needed
    # e.g. if 'number' has 3 digits then make sure 'powers' has all the values up to index 3*9 = 27
    while len(str(number)) * 9 > len(powers[1:]): # skip 0
        # we need more elements in 'powers'
        # powers[index] = index for all new elements added
        powers.append(len(powers)) # clever(?) way of doing it

print ("Result:", a[-1])
