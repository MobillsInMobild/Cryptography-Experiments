import exgcd
import Miler_Rabin
import modEx
import random
import math


def goodPrime(n):
    return Miler_Rabin.Miler_Rabin(n, 100)


def getGoodPrime(numBits):
    candidate = 1
    while goodPrime(candidate) == False:
        candidate = random.getrandbits(numBits)
        # print(candidate)
    return candidate


def getInverse(e, n):
    return (exgcd.exgcd(e, n)[1] + n) % n


"""
def getM(message):
    message = list(message)
    if len(message) % 2 == 1:
        message.append("{")
    lenM = len(message)//2
    m = []
    for i in range(lenM):
        m.append((ord(message[i*2])-ord("a")) *
                 100+(ord(message[i*2+1])-ord("a")))
    return m


def getMessage(m):
    message = []
    for i in range(len(m)):
        message.append(chr(m[i]//100+ord("a")))
        message.append(chr(m[i] % 100+ord("a")))
    if message[-1] == "{":
        message.pop()
    return "".join(message)


    def outMessage(m):
    for i in range(len(m)):
        m[i]=str(m[i])
        m[i]="0"*(4-len(m[i]))+m[i]
    return "".join(m)

def outMessage2m(message):
    lenMessage=len(message)
    M=[]
    if lenMessage%4!=0:
        print("Error:outMessage2m")
        return
    else:
        lenM=lenMessage//4
        for i in range(lenM):
            M.append(int(message[i*4:i*4+4]))
        return M
 """


class RSA:
    def setm(self, m):
        self.m = m
        self.result = m

    def getKeys(self, numBits=500, seed=None):
        self.p = getGoodPrime(numBits)
        self.q = getGoodPrime(numBits)
        varphi = (self.p - 1) * (self.q - 1)
        if seed == None:
            self.e = 3
            while exgcd.gcd(self.e, varphi) != 1:
                self.p = getGoodPrime(numBits)
                self.q = getGoodPrime(numBits)
                varphi = (self.p - 1) * (self.q - 1)
        else:
            self.e = seed
            while exgcd.gcd(self.e, varphi) != 1:
                self.p = getGoodPrime(numBits)
                self.q = getGoodPrime(numBits)
                varphi = (self.p - 1) * (self.q - 1)
        self.n = self.p * self.q
        self.d = getInverse(self.e, varphi)

    def showInfo(self):
        print("p=%d" % self.p)
        print("q=%d" % self.q)
        print("n=%d" % self.n)
        print("e=%d" % self.e)
        print("d=%d" % self.d)

    def RSA_encrypt(self):
        self.result = modEx.quick_modEx(self.m, self.e, self.n)

    def setInfo(self, p, q, d):
        self.p = p
        self.q = q
        self.d = d
        varphi = (self.p - 1) * (self.q - 1)
        self.n = self.p * self.q
        self.e = getInverse(self.d, varphi)

    def RSA_decrypt(self):
        # 用于加速运算
        d_Mod_p = self.d % (self.p - 1)
        d_Mod_q = self.d % (self.q - 1)
        Vp = modEx.quick_modEx(self.m, d_Mod_p, self.p)
        Vq = modEx.quick_modEx(self.m, d_Mod_q, self.q)
        Xp = self.q * (getInverse(self.q, self.p))
        Xq = self.p * (getInverse(self.p, self.q))
        #print(Vp*Xp+Vq*Xq)
        self.result = (Vp * Xp + Vq * Xq) % self.n


if __name__ == "__main__":
    message = int(input("Please input your message\n"))
    operation = input(
        "Please input your operation: e(encrypt) or d(decrypt)\n")
    if operation == "e":
        rsa = RSA(message)
        rsa.getKeys()
        rsa.showInfo()
        rsa.RSA_encrypt()
        print(rsa.result)
    #  print(outMessage(rsa.result))
    elif operation == "d":
        rsa = RSA(message)
        p = int(input("Please input your p\n"))
        q = int(input("Please input your q\n"))
        d = int(input("Please input your d\n"))
        rsa.setInfo(p, q, d)
        rsa.showInfo()
        rsa.RSA_decrypt()
        print(rsa.result)
