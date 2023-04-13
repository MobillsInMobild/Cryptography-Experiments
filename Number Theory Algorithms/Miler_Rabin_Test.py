from random import randint
from math import sqrt
def quick_modEx(a,b,c):
    ans=1
    while(int(b)>0):
        if b%2==1:
            ans=(ans*a)%c
            b=(b-1)//2
        else:
            b=b//2
        a=(a*a)%c    
    return ans

# 返回False为合数，反之为素数

def Miler_Rabin(n,t):
    k=0
    cur=n-1
    while(cur%2==0):
        k+=+1
        cur//=2
    q=cur
    for i in range(0,t):
        a=randint(1,n-1)
        flag=0 #flag=1表示不确定
        if  quick_modEx(a,q,n)==1:
            flag=1
            continue
        for j in range(0,k):
            if(quick_modEx(a,2**j*q,n)==n-1):
                flag=1
                break
        if(flag==0):
            return False
    return True

def isprime(a):
    flag=True
    if(a==2):
        return True
    for i in range(2,int(sqrt(a))+2):
        if(a%i==0):
            flag=False
    return flag
    

n=100000
for t in range(1,100):
    acNum=0
    accuracy=0
    for i in range(2,n):
        if(Miler_Rabin(i,t)==isprime(i)):
            acNum+=1
        else:
            print(i) 
    accuracy=acNum/(n-2)
    print("time:%d acNum:%d  accuracy:%f"%(t,acNum,accuracy))

