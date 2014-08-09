import math

'''
primeFactorization() function has been originally written to solve Problem 3

Files using this function:
euler005.py
'''
def primeFactorization (n):
    """Returns sorted list of prime factors of n"""
    # all the prime factors that are < n are also <= sqrt(n)
    limit = int (math.sqrt(n))

    while limit > 0:
        # factors found        
        if n % limit == 0:
            # if limit == 1 then n must be prime
            if limit == 1:
                return [n]
            # try to factorize the factors found
            else:
                return sorted (primeFactorization(limit) + primeFactorization(n//limit))
        limit -= 1

'''
listOfPrimes() function has been originally written to solve Problem 7

Files using this function:
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
