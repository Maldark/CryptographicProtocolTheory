from fractions import gcd
import random

def PrimalityTest(n):
    if n == 2:
        return True
    if n & 1 == 0: # Cannot be an even number
        return False
    
    k = 0
    m = n - 1
    while m & 1 == 0:
        k += 1
        m = m >> 1 # Divide by two

    a = random.randint(1, n-2)
    b = pow(a, m, n)

    if b % n == 1:
        return True

    for i in range(0, k):
        if b % n == (-1 % n):
            return True
        b = pow(b, 2, n)
    
    return False