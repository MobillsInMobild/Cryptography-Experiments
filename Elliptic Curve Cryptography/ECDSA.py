import hashlib
import random
import EC
import exgcd


def getSHA2(data):
    sha2 = hashlib.sha256()
    sha2.update(data.encode("utf-8"))
    return int(sha2.hexdigest(), 16)


# 椭圆曲线数字签名
"""
Q表示公钥,d表示私钥
S表示签名对
"""


class ECDSA:
    def __init__(self, G, field):
        self.G = G
        self.field = field

    def setN(self, n):
        self.n = n

    def getKey(self):
        self.d = random.randint(1, self.n - 1)
        self.Q = self.G.quick_multiply(self.d)

    def setM(self, m):
        self.m = m

    def Signature(self):
        while True:
            k = random.randint(1, self.n - 1)
            P = self.G.quick_multiply(k)
            r = (P.x) % self.n
            if r != 0:
                e = getSHA2(self.m)
                t = exgcd.getInverse(k, self.n)
                s = (t * (e + self.d * r)) % self.n
                if s != 0:
                    self.S = [r, s]
                    return self.S

    def verification(self, m, S):
        r = S[0]
        s = S[1]
        if r > self.n or r < 1 or s > self.n or s < 1:
            print("1:")
            return False
        else:
            e = getSHA2(m)
            w = exgcd.getInverse(s, self.n)
            u1 = e * w
            u2 = r * w
            C1=self.G.quick_multiply(u1)
            C2=self.Q.quick_multiply(u2)
            X = C1.add(C2)
            if X.isO == True:
                print("2:")
                return False
            else:
                v = (X.x) % self.n
                if v == r:
                    return True
                else:
                    print("3:")
                    print(v)
                    return False


if __name__ == "__main__":
    m = "test123666"
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    field = EC.Field(a, b, p)
    G = EC.EC(
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        field)
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    ecdsa = ECDSA(G, field)
    ecdsa.setN(n)
    ecdsa.getKey()
    ecdsa.setM(m)
    print(ecdsa.Signature())
    print(ecdsa.verification(m, ecdsa.S))
    print(ecdsa.verification(m+"1", ecdsa.S))
