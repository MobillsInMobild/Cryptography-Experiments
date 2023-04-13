import RSA
import key
import random
import exgcd
import modEx

class voter:
    def setKey_CTF(self,N,E):
        self.N=N
        self.E=E

    def getKey(self):
        info=key.getKeys(30)
        self.p=info[0]
        self.q=info[1]
        self.n=info[2]
        self.e=info[3]
        self.d=info[4]
    
    def setM(self,m):
        self.m=m

    # 盲化公钥
    def blind(self):
        self.r=random.randint(2,self.N)
        while exgcd.gcd(self.r,self.N)!=1:
            self.r=random.randint(2,self.N)
        self.e_=(self.e*modEx.quick_modEx(self.r,self.E,self.N))%self.N
        #print("%d=(%d*modEx.quick_modEx(%d,%d,%d))mod %d"%(self.e_,self.e,self.r,self.E,self.N,self.N))



    # 去盲化
    def unblind(self,e_Signed):
        self.c=(e_Signed*exgcd.getInverse(self.r,self.N)%self.N)%self.N
        #print("%d=%d*exgcd.getInverse(%d,%d)mod%d"%(self.c,e_Signed,self.r,self.N,self.N))


    
    # 加密
    def signM(self):
        self.m_=RSA.RSA_encrypt(self.m,self.d,self.n)
    

    def show(self):
        print("p:%d"%self.p)
        print("q:%d"%self.q)
        print("n:%d"%self.n)
        print("e:%d"%self.e)
        print("d:%d"%self.d)
        print("c:%d"%self.c)
        print("e_:%d"%self.e_)
        print("r:%d"%self.r)



    def register(self,m,E,N):
        self.setM(m)
        self.getKey()
        self.setKey_CTF(N,E)
        self.blind()


