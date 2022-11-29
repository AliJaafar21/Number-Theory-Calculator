def FastExponentiation(a, b, n):

    binary = "{0:b}".format(b)
    
    result = 1
    for i in range(len(binary)):
        result = (result * result) % n
        if binary[i] == '1':
            result = (result * a) % n
    
    return result
