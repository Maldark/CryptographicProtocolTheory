import random
from Algorithms import modinv, primality_test
import math

import decimal

PRIMALITY_CERTAINTY = 20 # Repetitions of Miller-Rabin primality test

def __generate_k_bit_number(k):
    # Generating prime in range [sqrt(2) * 2^{k/2 - 1} , 2^{k/2}] supposedly
    # ensures a K-bit key when multiplying primes together
    # https://crypto.stackexchange.com/questions/19263/generation-of-n-bit-prime-numbers-what-is-the-actual-range
    return random.randint(math.floor(math.sqrt(2) * pow(2, k // 2 - 1)), pow(2, k // 2))

def __generate_k_bit_prime(k):
    while True:
        p = __generate_k_bit_number(k)
        if primality_test(PRIMALITY_CERTAINTY, p):
            return p

def keygen(k):
    p = __generate_k_bit_prime(k)
    q = __generate_k_bit_prime(k)

    n = p * q
    phi = (p-1)*(q-1)

    while True:
        e = random.randint(1, phi)
        if math.gcd(e, phi) == 1:
            break
    d = modinv(e, phi)

    pk = {'n': n, 'e': e}
    sk = {'p': p, 'q': q, 'd': d}

    return pk, sk

def encrypt(pk, x):
    n = pk['n']
    e = pk['e']

    return pow(x, e, n)

def decrypt(sk, y):
    p = sk['p']
    q = sk['q']
    d = sk['d']

    n = p*q
    
    return pow(y, d, n)