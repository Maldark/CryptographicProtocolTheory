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
        m = m // 2

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

def modinv(b, a):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    # q = math.floor(a0 / b0)
    # r = a0 - q * b0
    q, r = divmod(a0, b0)
    while r > 0:
        temp = (t0 - q * t) % a
        t0 = t
        t = temp
        a0 = b0
        b0 = r
        q, r = divmod(a0, b0)

    if b0 != 1:
        raise Exception('modular inverse does not exist')
    else:
        return t


def square_and_multiply(base, exponent, modulus):
    pass