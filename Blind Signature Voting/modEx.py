def modeEx(a,b,c):
    i=0
    ans=1
    for i in range(0,b):
        ans=((ans%c)*(a%c))%c
    return ans

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

if __name__ == "__main__":
    a=int(input("Please input your a\n"))
    b=int(input("Please input your b\n"))
    c=int(input("Please input your c\n"))

    print(modeEx(a,b,c))
    print(quick_modEx(a,b,c))