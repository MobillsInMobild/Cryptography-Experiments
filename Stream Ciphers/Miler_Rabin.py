from random import randint
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

if __name__=="__main__":
    n=int(input("Please input your n\n"))
    t=int(input("Please input your times\n"))
    print(Miler_Rabin(n,t))   