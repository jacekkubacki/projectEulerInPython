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
'''
def listOfPrimes (n):
    """Returns ordered list of primes in range(2,n)"""
    if n < 2 : return []
    primeNumbers = []
    
    for n in range(3, n, 2): # check only odd numbers
        isPrime = True
        for p in primeNumbers:
        # we only want to check the primes <= sqrt(n)
        # see: http://en.wikipedia.org/wiki/Prime_number#Trial_division
            if p <= math.sqrt(n):
                if n % p == 0:
                    isPrime = False
                    break
            else:
                break
        if isPrime:
            primeNumbers.append(n)

    return [2] + primeNumbers
