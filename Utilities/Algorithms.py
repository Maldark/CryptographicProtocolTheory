import math
import random

def miller_rabin(n):
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

def primality_test(k, n):
    for i in range(k):
        if not miller_rabin(n):
            return False

    return True

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m