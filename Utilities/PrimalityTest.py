import MillerRabin

def PrimalityTest(k, n):
    for i in range(k):
        if not MillerRabin.PrimalityTest(n):
            return False

    return True