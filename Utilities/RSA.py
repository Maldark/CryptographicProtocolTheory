import random
from PrimalityTest import PrimalityTest

PRIMALITY_CERTAINTY = 20 # Repetitions of Miller-Rabin primality test

def __generate_k_bit_number(k):
    return random.randint(0, 2**k - 1)

def __generate_k_bit_prime(k):
    while True:
        p = __generate_k_bit_number(k)
        if PrimalityTest(PRIMALITY_CERTAINTY, p):
            return p

def keygen(k):
    p = __generate_k_bit_prime(k)
    q = __generate_k_bit_prime(k)
    pass

def encrypt(pk, x):
    pass

def decrypt(sk, y):
    pass