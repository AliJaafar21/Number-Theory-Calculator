import random
from .FastExponentiation import FastExponentiation

#returns 1 if number is maybe prime | 0 if composite | -1 if timeout
def MillerRabin(n):

    #finds integers k, q such that n-1=2^k*q
    def findIntegers(n):
        k=1
        while True:
            q = (n-1)//(2**k)
            #if q is not an integer
            if (n-1!=q*(2**k)):
                continue
            #if q is even
            if (q%2==0): 
                k+=1
                continue
            #q is odd
            else:
                return [k, q]
    
    #return maybe prime if n=0,1,2,3
    if n<=3:
        return 1

    #return 0 for even numbers
    if (n%2 ==0):
        return 0

    findIntegersResult = findIntegers(n)
    k, q = findIntegersResult[0], findIntegersResult[1]

    #select random integer a between 1 and n-1
    a = random.randint(1, n-1)
    if FastExponentiation(a, q, n) == 1:
        #maybe prime
        return True

    #iterate k times
    for j in range(k):
        exp1 = 2 ** j
        exp2= q * exp1
        if FastExponentiation(a, exp2, n) == n - 1:
            #maybe prime
            return 1 

    #composite
    return 0
