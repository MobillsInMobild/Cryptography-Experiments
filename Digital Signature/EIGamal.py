import random
import modEx
import exgcd
import hashlib


def getInverse(e, n):
    return (exgcd.exgcd(e, n)[1] + n) % n


class EIGamal:
    def set_m(self, m):
        self.m = m

    def set_aq(self, a, q):
        self.a = a
        self.q = q

    def get_Key(self):
        self.X_A = random.randint(2, self.q - 2)
        self.Y_A = modEx.quick_modEx(self.a, self.X_A, self.q)

    def set_Key(self, X_A, Y_A):
        self.X_A = X_A
        self.Y_A = Y_A

    def dis_Key(self):
        print("Public Key:{q,a,Y_A}={%d,%d,%d}" % (self.q, self.a, self.Y_A))
        print("Private Key:{X_A}={%d}" % (self.X_A))

    def get_K(self):
        self.K = 2
        while exgcd.gcd(self.K, self.q - 1) != 1:
            self.K = random.randint(1, self.q - 1)

    def set_K(self, K):
        self.K = K

    def get_Signature(self):
        self.S_1 = modEx.quick_modEx(self.a, self.K, self.q)
        K_Inverse = getInverse(self.K, self.q - 1)
        self.S_2 = (K_Inverse * (self.m - self.X_A * self.S_1)) % (self.q - 1)

    def verify(self, S_1, S_2):
        V_1 = modEx.quick_modEx(self.a, self.m, self.q)
        V_2 = (modEx.quick_modEx(self.Y_A, S_1, self.q) *
               modEx.quick_modEx(S_1, S_2, self.q)) % self.q
        if V_1 == V_2:
            return True
        else:
            return False


if __name__ == "__main__":
    test = EIGamal()
    test.set_aq(10, 19)
    test.get_Key()
    #test.set_Key(16,4)
    test.dis_Key()
    test.set_m(14)
    test.get_K()
    #test.set_K(5)
    test.get_Signature()

    print(test.verify(test.S_1, test.S_2))
    print((test.S_1, test.S_2))
    print(test.verify(test.S_1 + 1, test.S_2))
