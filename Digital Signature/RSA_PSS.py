import math
import hashlib
import random
import RSA

hLen = 20
sLen = 20


def MGF1(X, maskLen):
    T = ""
    k = math.ceil(maskLen / hLen) - 1
    for counter in range(0, k + 1):
        C = bin(counter)[2:].zfill(32)
        T = T + hashlib.sha1((X + C).encode("utf-8")).hexdigest()
    mask = T[:maskLen * 2]
    return mask


def get_Salt(sLen):
    Salt = hex(random.getrandbits(sLen * 8))[2:]
    return Salt


class RSA_PSS:
    def __init__(self):
        self.rsa = RSA.RSA()
        self.rsa.getKeys()
        self.n = self.rsa.n
        self.emBits = len(bin(self.n)[2:]) - 1
        self.emLen = math.ceil(self.emBits / 8)
        self.bc = "bc"
        self.padding1 = "0000000000000000"
        self.hLen = hLen
        self.sLen = sLen
        temp = []
        for i in range(self.emLen - self.hLen - self.sLen - 2):
            temp.append("00")
        temp.append("01")
        self.padding2 = "".join(temp)

    def get_Signature(self, M):
        mHash = hashlib.sha1(M.encode("utf-8")).hexdigest()
        salt = get_Salt(sLen)
        _M = self.padding1 + mHash + salt
        H = hashlib.sha1(_M.encode("utf-8")).hexdigest()
        DB = self.padding2 + salt
        MGF = MGF1(H, self.emLen - self.hLen - 1)
        maskedDB = int(DB, 16) ^ int(MGF, 16)
        maskedDB = bin(maskedDB)[2:].zfill(len(DB) * 4)
        maskedDB = list(maskedDB)
        for i in range(8 * self.emLen - self.emBits):
            maskedDB[i] = "0"
        maskedDB = hex(int("".join(maskedDB), 2))[2:].zfill(len(DB))
        EM = maskedDB + H + self.bc
        m = int(EM, 16)
        self.rsa.setm(m)
        self.rsa.RSA_encrypt()
        self.S = hex(self.rsa.result)[2:]
        self.M = M

    def verify(self, M, S):
        s = int(S, 16)
        self.rsa.setm(s)
        self.rsa.RSA_decrypt()
        m = self.rsa.result
        mHash = hashlib.sha1(M.encode("utf-8")).hexdigest()
        EM = hex(m)[2:]
        emLen = len(EM) // 2
        # 如果 emLen<hLen+sLen+2，输出 False
        if emLen < self.hLen + self.sLen + 2:
            print("False:0")
            return False
        emBits = len(bin(self.rsa.n)[2:]) - 1
        emLen = math.ceil(emBits / 8)
        EM = EM.zfill(emLen * 2)
        # 如果EM 的最右字节不是十六进制值BC，输出 False
        if EM.endswith(self.bc) == False:
            print("False:1")
            return False
        maskDB = EM[:(emLen - self.hLen - 1) * 2]
        H = EM[(emLen - self.hLen - 1) * 2:(emLen - self.hLen - 1) * 2 +
               self.hLen * 2]
        # 如果maskedDB最左 8emLen-emBits位不全是0，输出 False
        tmp = bin(int(maskDB[:2], 16))[2:].zfill(4 * len(maskDB))
        prefix = []
        for _ in range(8 * emLen - emBits):
            prefix.append("0")
        prefix = "".join(prefix)
        if tmp.startswith(prefix) == False:
            print("False:2")
            return False
        dbMask = MGF1(H, emLen - self.hLen - 1)
        DB = int(maskDB, 16) ^ int(dbMask, 16)
        DB = bin(DB)[2:].zfill(len(maskDB) * 4)
        DB = list(DB)
        for i in range(8 * emLen - emBits):
            DB[i] = "0"
        # 如果DB 的最左 emLen-hLen-sLen-1 字节不等于填充2，则输出 False
        DB = hex(int("".join(DB), 2))[2:].zfill(len(maskDB))
        if DB[:(emLen - self.hLen - self.sLen - 1) * 2] != self.padding2:
            return False
        salt = DB[len(DB) - self.sLen * 2:]
        _M = self.padding1 + mHash + salt
        _H = hashlib.sha1(_M.encode("utf-8")).hexdigest()
        if H == _H:
            return True
        else:
            print("False:3")
            return False


if __name__ == "__main__":
    test = RSA_PSS()
    test.get_Signature("hello")
    print(test.verify(test.M, test.S))
    print((test.M,test.S))
    print(test.verify(test.M + "1", test.S))
