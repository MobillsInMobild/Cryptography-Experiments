import Miler_Rabin
import exgcd
import random


def goodPrime(n):
    return n % 4 == 3 and Miler_Rabin.Miler_Rabin(n, 100)

def getGoodPrime(numBits=512):
    candidate = 1
    while goodPrime(candidate)==False:
        candidate = random.getrandbits(numBits)
    return candidate


def parity(n):
    return int(bin(n)[-1])


def BBS(numBits,seed=None):
    if seed==None:
        p=getGoodPrime()
        q=getGoodPrime()
        n=p*q
    else:
        p,q=seed
        n=p*q
    s=getGoodPrime()
    while exgcd.gcd(s,p)!=1 or exgcd.gcd(s,q)!=1:
        s=getGoodPrime()
    lst=[]
    x=Miler_Rabin.quick_modEx(s,2,n)
    for i in range(numBits):
        x=Miler_Rabin.quick_modEx(x,2,n)
        lst.append(parity(x))
    return lst

if __name__=="__main__":
    numBits=int(input("Please input your numBits"))
    print(BBS(numBits))
    

