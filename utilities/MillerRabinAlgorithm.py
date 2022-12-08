import random

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

#returns True if number is maybe prime and false if composite
def MillerRabin(n):
    #return maybe prime if n=0,1,2,3
    if n<=3:
        return True
    #return false for even numbers
    if (n%2 ==0):
        return False
    #find integers k and q such that n-1==2^k*q
    k,q = findIntegers(n)[0], findIntegers(n)[1]
    #select random integer a between 1 and n-1
    a = random.randint(1, n-1)
    if (a**q % n ==1):
        #maybe prime
        return True
    #iterate k times
    for j in range(k):
        exp1 = 2**j
        exp2= q*exp1
        if ((a**exp2)%n)== n-1:
            #maybe prime
            return True 
    #composite
    return False

 