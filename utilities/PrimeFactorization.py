def PrimeFactorization(n):
    
    if n == 0 or n == 1:
        return {n: 1}

    factors = {}

    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n = n // 2;
    if exponent != 0:
        factors[2] = exponent

    i = 3
    while i * i <= n:
        exponent = 0
        while n % i == 0:
            exponent += 1
            n = n // i 
        if exponent != 0:
            factors[i] = exponent
        i += 2    

    if n > 2:
        factors[n] = 1

    return factors
