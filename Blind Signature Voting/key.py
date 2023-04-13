import random
import Miler_Rabin
import exgcd
import modEx

def goodPrime(n):
    return Miler_Rabin.Miler_Rabin(n, 100)


def getGoodPrime(numBits):
    candidate = 1
    while goodPrime(candidate) == False:
        candidate = random.getrandbits(numBits)
        # print(candidate)
    return candidate


def getKeys(numBits):
    p = getGoodPrime(numBits)
    q = getGoodPrime(numBits)
    n = p*q
    varphi = (p-1)*(q-1)
    e=random.randint(2,varphi)
    while exgcd.gcd(e,varphi)!=1:
        e=random.randint(2,varphi)
    d = exgcd.getInverse(e, varphi)
    return [p,q,n,e,d]

if __name__ == "__main__":
    print(getKeys(4))