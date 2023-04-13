import EC
# 椭圆曲线加解密
"""
P_A表示公钥,n_A表示私钥
C_m表示密文
P_m表示明文
"""
class ECC:
    def __init__(self,G,field):
        self.G=G
        self.field=field
        
    def setMessage(self,P_m):
        self.P_m=P_m    

    def setPrivateKey(self,n_A):
        self.n_A=n_A
    
    def getPublicKey(self):
        self.P_A=self.G.quick_multiply(self.n_A)

    def encrypt(self,k):
        a=self.G.quick_multiply(k)
        b=self.P_m.add(self.P_A.quick_multiply(k))
        self.C_m=[a,b]
        return self.C_m

    def decrypt(self,C_m,n_A):
        P_m=C_m[1].minus(C_m[0].quick_multiply(n_A))
        return P_m



if __name__ == "__main__":
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    field=EC.Field(a,b,p)
    G=EC.EC(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 ,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,field)
    ecc=ECC(G,field)
    print("Message:")
    (G.quick_multiply(2)).show()
    ecc.setMessage(G.quick_multiply(2))
    ecc.setPrivateKey(65949)
    ecc.getPublicKey()
    C_m=ecc.encrypt(5)
    print("Encrypt:")
    C_m[0].show()
    C_m[1].show()
    print("Decrypt:")
    (ecc.decrypt(ecc.C_m,ecc.n_A)).show()
