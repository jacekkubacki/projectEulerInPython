import math

def primeFactorization (n):
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
