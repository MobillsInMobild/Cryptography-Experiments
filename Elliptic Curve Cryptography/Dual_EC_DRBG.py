import EC
from random import randint 

def lsb(s, i):
    return s & ((1 << i) - 1)

class ECPRNG:
    def __init__(self,field,G,n):
        self.field = field
        self.G=G
        self.n = n
        temp = randint(2, self.n)
        self.Q=self.G.quick_multiply(temp)
    
    def PRNG(self, k):
        s = randint(0, self.n)
        tmp = []
        for _ in range(k):
            s = self.G.quick_multiply(s).x
            r = lsb(self.Q.quick_multiply(s).x, 240)
            tmp.append(bin(r)[2:])
        return tmp

if __name__ == "__main__":
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    field=EC.Field(a,b,p)
    G = EC.EC(
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        field)
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    test = ECPRNG(field,G,n)

    k = int(input("Please input your k"))
    print(test.PRNG(k))