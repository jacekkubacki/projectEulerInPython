import itertools
import math
import re
import string


'''
arithmeticSum() function has been originally written to solve Problem 1

Files using this function:
euler001.py
euler023.py
'''
def arithmeticSum(a1, diff, n):
    """Returns sum of arithmetic progression"""
    return (2 * a1 + (n - 1) * diff) * (n / 2.0)


'''
dequote() function has been originally written to solve Problem 22

Files using this function:
euler022.py
euler042.py
'''
def dequote(s):
    """Returns the string with leading and trailing double quote character removed"""
    return re.sub(r'^"|"$', '', s)


'''
isPrime() has been written to solve Problem 7

Files using this function:
euler007.py
euler027.py
euler041.py
'''
def isPrime (number):
    """Returns True is number is prime, False otherwise"""
    # This algorithm checks if the given number can be divided by integers of the form 6k +/- 1
    # see: http://en.wikipedia.org/wiki/Primality_test#Naive_methods
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


'''
listOfDivisors() has been written to solve Problem 23

Files using this function:
euler021.py
euler023.py
'''
def listOfDivisors(number):
    """Returns list of numbers less than n which divide evenly into n"""
    if number <= 1:
        return []

    divisors = set([1])
    factors = primeFactors(number)

    for r in range(1, len(factors)):
        for c in itertools.combinations(factors, r):
            n = 1
            for d in c:
                n *= d
            divisors.add(n)

    return list(divisors)


'''
listOfPrimes() function has been originally written to solve Problem 7

Files using listOfPrimes function:
euler010.py
euler027.py
euler035.py
euler049.py
euler050.py
'''
def listOfPrimes (n):
    """Returns ordered list of primes in range(2,n)"""
    """using linear sieve algorithm: http://edu.i-lo.tarnow.pl/inf/alg/001_search/0012.php"""
    primes = [True for i in range(0, n)]
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

    return [i for i in range(2, n) if primes[i]]


'''
primeFactors() function has been originally written to solve Problem 3

Files using this function:
euler003.py
euler005.py
euler012.py
euler023.py
'''
def primeFactors(n):
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
sumOfDigits() function has been originally written to solve Problem 119

Files using this function:
euler016.py
euler056.py
euler119.py
'''
def sumOfDigits(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s


'''
wordValue() function has been originally written to solve Problem 22

Files using this function:
euler022.py
euler042.py
'''
alphabet = [''] + list(string.ascii_uppercase)
def wordValue(s):
    """Converts each letter in a word to a number corresponding to its alphabetical position and adds these values"""
    word = list (s.upper())
    result = 0
    for letter in word:
        result += alphabet.index(letter)

    return result
