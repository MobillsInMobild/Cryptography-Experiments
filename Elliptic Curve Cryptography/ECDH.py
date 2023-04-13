import EC
import random

class ECDH:
    def __init__(self,G,field):
        self.G=G
        self.field=field

    def setN(self, n):
        self.n = n
    
    def getPublickey(self):
        self.n_A=random.randint(1,self.n)
        self.P_A=self.G.multiply(self.n_A)
        self.n_B=random.randint(1,self.n)
        self.P_B=self.G.multiply(self.n_B)

    def setPublickey(self,n_A,n_B):
        self.n_A=n_A
        self.P_A=self.G.multiply(self.n_A)
        self.n_B=n_B
        self.P_B=self.G.multiply(self.n_B)


    def getKey(self):
        self.K1=self.P_B.multiply(self.n_A)
        self.K2=self.P_A.multiply(self.n_B)
        self.K1.show()
        self.K2.show()


if __name__ == "__main__":
    p=211
    a=0
    b=-4
    field = EC.Field(a, b, p)
    G=EC.EC(2,2,field)
    ecdh=ECDH(G,field)
    ecdh.setPublickey(121,203)
    ecdh.getKey()


