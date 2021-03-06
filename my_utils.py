"""
This module contains functions used by two or more solutions.
There is no error checking to speed up the execution.
"""
import itertools
import math
import re
import string


def arithmetic_sum(a1, diff, n):
    """Return sum of arithmetic progression"""
    return (2 * a1 + (n - 1) * diff) * (n / 2.0)


def dequote(s):
    """Return the string with leading and trailing double quote character removed"""
    return re.sub(r'^"|"$', '', s)


def is_prime(number):
    """Return True is number is prime, False otherwise"""
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


def list_of_divisors(number):
    """Return list of numbers less than n which divide evenly into n"""
    if number <= 1:
        return []

    divisors = {1}
    factors = list_of_prime_factors(number)

    for r in range(1, len(factors)):
        for c in itertools.combinations(factors, r):
            n = 1
            for d in c:
                n *= d
            divisors.add(n)

    return list(divisors)


def list_of_primes(n):
    """Return ordered list of primes in range(2,n)"""
    # linear sieve algorithm: http://edu.i-lo.tarnow.pl/inf/alg/001_search/0012.php
    primes = [True] * n
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
                if primes[q]:
                    break
        while True:
            p += 1
            if primes[p]:
                break

    return [i for i in range(2, n) if primes[i]]


def list_of_prime_factors(n):
    """Return UNSORTED list of prime factors of n"""
    # all the prime factors that are < n are also <= sqrt(n)
    limit = int(math.sqrt(n))

    # let's start with 2 to break down even numbers
    for i in range(2, limit + 1):
        if n % i == 0:
            # factors found, try to factorize them
            return list_of_prime_factors(i) + list_of_prime_factors(n // i)
    else:
        # no factors found, must be prime  
        return [n]
    

def sum_of_digits(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s


# global variable
alphabet = [''] + list(string.ascii_uppercase)


def word_value(s):
    """Convert each letter in a word to a number corresponding to its alphabetical position and add these values"""
    word = list(s.upper())
    result = 0
    for letter in word:
        result += alphabet.index(letter)

    return result
