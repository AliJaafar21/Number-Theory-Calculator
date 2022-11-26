def PrimeFactorization(number):

    if number == 0 or number == 1:
        return {number: 1}

    factors = {}
    divisor = 2
    exponent = 0

    while number > 1:
        if number % divisor == 0:
            number /= divisor
            exponent += 1
        else:
            if exponent != 0:
                factors[divisor] = exponent
            divisor += 1
            exponent = 0

    if exponent != 0:
        factors[divisor] = exponent

    return factors
