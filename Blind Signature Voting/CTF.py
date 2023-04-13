import RSA
import key
import random
import exgcd
import modEx


class CTF:
    def getKey(self):
        info = key.getKeys(30)
        self.P = info[0]
        self.Q = info[1]
        self.N = info[2]
        self.E = info[3]
        self.D = info[4]


    # 加密
    def signE_(self, e_):
        self.e_Signed = RSA.RSA_encrypt(e_, self.D, self.N)
        #print("%d= RSA.RSA_encrypt(%d, %d, %d)"%(self.e_Signed,e_, self.D, self.N))


    def receive(self, e, m, m_, c,n):
        self.e = e
        self.m = m
        self.m_ = m_
        self.c = c
        self.n=n

    # 检验 e
    def verifye(self, e, c):
        eSigned=RSA.RSA_encrypt(e,  self.D, self.N)
        #print("eSigned=%d"%RSA.RSA_encrypt(self.e,  self.D, self.N))
        if c == eSigned:
            print("True")
            return True
        else:
            print("False:verifyP_")
            return False

    # 检验 m_
    def verifyM_(self, m, m_):
        mUnsigned = RSA.RSA_encrypt(m_, self.e, self.n)
        if mUnsigned == m:
            print("True")
            return True
        else:
            print("False:verifyM_")
            return False

    def show(self):
        print("P:%d"%self.P)
        print("Q:%d"%self.Q)
        print("N:%d"%self.N)
        print("E:%d"%self.E)
        print("D:%d"%self.D)
        print("e_Signed:%d"%self.e_Signed)


    def register(self):
        self.getKey()

