import getDigitsPrime
import modEx
import random
import hashlib
import Miler_Rabin
import exgcd


def getInverse(e, n):
    return (exgcd.exgcd(e, n)[1] + n) % n


class Schnorr:
    def set_M(self, M):
        self.M = M

    def get_pq(self):
        self.q = getDigitsPrime.getDigitsPrime(160)
        p = (self.q << (1024 - 160)) + 1
        while Miler_Rabin.Miler_Rabin(p, 10) == False:
            p = (p - 1) + self.q + 1
        self.p = p

    def set_pq(self, p, q):
        if (p - 1) % q == 0:
            self.p = p
            self.q = q
        else:
            print("Error:p-1 is not divisible by q")

    def get_a(self):
        a = 1
        while a == 1:
            h = random.randint(1, self.p)
            a = modEx.quick_modEx(h, (self.p - 1) // self.q, self.p)
        self.a = a
        
    def set_a(self, a):
        if modEx.quick_modEx(a, self.q, self.p) == 1:
            self.a = a
        else:
            print("Error:a is unsuitable for p and q")

    def dis_pqa(self):
        print("{p,q,a}={%d,%d,%d}" % (self.p, self.q, self.a))

    def get_Key(self):
        self.s = random.randint(1, self.q - 1)
        self.v = modEx.quick_modEx(self.a, self.s, self.p)
        self.v = getInverse(self.v, self.p)

    def dis_Key(self):
        print("Public Key:{v}={%d}" % (self.v))
        print("Private Key:{s}={%d}" % (self.s))

    def get_Signature(self):
        self.r = random.randint(1, self.q - 1)
        self.x = modEx.quick_modEx(self.a, self.r, self.p)
        hashSHA1 = hashlib.sha1()
        #print(self.M)
        #print(self.x)
        hashSHA1.update((str(self.M) + str(self.x)).encode("utf-8"))
        self.e = int(hashSHA1.hexdigest(), 16)
        self.y = (self.r + self.s * self.e) % self.q

    def dis_Signature(self):
        print("(e,y)=(%d,%d)" % (self.e, self.y))

    def verify(self, e, y):
        _x = (modEx.quick_modEx(self.a, y, self.p) *
              modEx.quick_modEx(self.v, e, self.p)) % self.p
        hashSHA1 = hashlib.sha1()
        #print(self.M)
        #print(_x)
        hashSHA1.update((str(self.M) + str(_x)).encode("utf-8"))
        _e = int(hashSHA1.hexdigest(), 16)
        if self.e == _e:
            return True
        else:
            #print(self.e)
            #print(_e)
            return False


if __name__ == "__main__":
    test = Schnorr()
    test.set_M(123456789)
    test.get_pq()
    test.get_a()
    #test.dis_pqa()
    test.get_Key()
    #test.dis_Key()
    test.get_Signature()
    test.dis_Signature()
    print(test.verify(test.e, test.y))
    print((test.e,test.y))
    print(test.verify(test.e + 1, test.y))
