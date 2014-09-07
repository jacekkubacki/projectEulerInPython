#!/usr/local/bin/python3
'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

units = [len(s) for s in ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
tens = [len(s) for s in ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']]
teens = [len(s) for s in ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']]
hundreds = [len(s)-1 for s in ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']]

result = 0

for number in range (1, 1000):
    n = number

    # hundreds
    if n // 100:
        result += hundreds[n//100]
        if n % 100 == 0:
            # 100, 200, 300, ...
            continue
        else:
            # add 'and' for n hundred AND something
            result += len('and')

    # tens
    n %= 100
    if n // 10 > 1:
        result += tens[n//10]
        # if i % 10 != 0 then add '-'
    elif n // 10 == 1:
        #teens
        result += teens[n%10]
        continue

    # units
    n %= 10
    result += units[n]

result += len ('one') + len ('thousand')

print ("Result:", result)
