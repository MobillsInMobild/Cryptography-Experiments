import exgcd

# 有限域类
class Field:
    def __init__(self,a,b,p):
        self.a=a
        self.b=b
        self.p=p

# 椭圆曲线类
class EC:
    def __init__(self,x,y,field):
        self.x=x
        self.y=y
        self.field=field
        self.p = field.p
        self.a = field.a
        self.b = field.b

    # 判断是否
    def isO(self):
        if self.x==self.p+31 and self.y==0:
            return True
        else:
            return False

    def neg(self):
        self.x=self.x
        self.y=0-self.y+self.p

    def add(self,other):
        if self.isO()== False and other.isO()==False:
            if self.y+other.y!=0:
                if self.x==other.x and self.y==other.y:
                    k=((3*self.x**2+self.a)*exgcd.getInverse(2*self.y,self.p))%self.p
                else:
                    k=((self.y-other.y)*exgcd.getInverse((self.x-other.x),self.p))%self.p
                #print(k)
                xr=(k**2-self.x-other.x)%self.p
                yr=(k*(self.x-xr)-self.y)%self.p
                ans=EC(xr,yr,self.field)
                return ans
            else:
                return EC(self.p+31,0,self.field)
        else:
            if self.isO()==True:
                return other
            else:
                return self
    
    def minus(self,other):
        other.neg()
        return self.add(other)

    def multiply(self,num):
        ans=EC(self.p+31,0,self.field)
        for i in range(num):
            ans=self.add(ans)
        return ans

    def quick_multiply(self,num):
        ans=EC(self.p+31,0,self.field)
        cur=self
        while num>0:
            if num&1==1:
                ans=ans.add(cur)
            cur=cur.add(cur)
            num=num//2
        return ans
        
    def show(self):
        print((self.x,self.y))



if __name__ == "__main__":
    G=Field(1,1,23)
    a=EC(12,4,G)
    b=EC(18,20,G)
    b2=b.multiply(2)
    c=a.minus(b2)
    c.show()