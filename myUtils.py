import math
import re
import string

'''
primeFactorization() function has been originally written to solve Problem 3

Files using this function:
euler003.py
euler005.py
euler012.py
'''

def primeFactors (n):
    """Returns UNSORTED list of prime factors of n"""
    # all the prime factors that are < n are also <= sqrt(n)
    limit = int (math.sqrt(n))

    # let's start with 2 to break down even numbers
    for i in range (2, limit + 1):
        if n % i == 0:
            # factors found, try to factorize them
            return primeFactors(i) + primeFactors(n//i)
    else:
        # no factors found, must be prime  
        return [n]
    
'''
listOfPrimes() function has been originally written to solve Problem 7

Files using listOfPrimes function:
euler010.py
euler035.py
euler049.py
euler050.py
'''
def listOfPrimes (n):
    """Returns ordered list of primes in range(2,n)"""
    """using linear sieve algorithm: http://edu.i-lo.tarnow.pl/inf/alg/001_search/0012.php"""
    primes = [True for i in range (0,n)]
    p = 2
    while p * p < n:
        q = p
        while p * q < n:
            x = p * q
            while x < n:
                primes[x] = False
                x *= p
            while True:
                q += 1
                if primes[q]: break
        while True:
            p += 1
            if primes[p]: break

    return [i for i in range(2,n) if primes[i]]

'''
dequote() function has been originally written to solve Problem 22

Files using this function:
euler022.py
euler042.py
'''
def dequote(s):
    """Returns the string with leading and trailing double quote character removed"""
    return re.sub (r'^"|"$', '', s)

'''
wordScore() function has been originally written to solve Problem 22

Files using this function:
euler022.py
euler042.py
'''
alphabet = [''] + list (string.ascii_uppercase)
def wordValue(s):
    """Converts each letter in a word to a number corresponding to its alphabetical position and adds these values"""
    word = list (s.upper())
    result = 0
    for letter in word: 
        result += alphabet.index(letter)

    return result

'''
sumOfDigits() function has been originally written to solve Problem 119

Files using this function:
euler016.py
euler056.py
'''
def sumOfDigits (number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s
