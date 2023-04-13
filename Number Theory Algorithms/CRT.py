def exgcd(a,b):
    if b==0:
        return [a,1,0]
    else:
        d,x1,y1=exgcd(b,a%b)
        x0=y1
        y0=x1-a//b*y1
        return (d,x0,y0)

def CRT(a1,a2,a3,b1,b2,b3):
    ans=0
    M=a1*a2*a3
    e1=exgcd(M//a1,a1)[1]
    e2=exgcd(M//a2,a2)[1]
    e3=exgcd(M//a3,a3)[1]
    while e1<0:
        e1=e1+a1
    while e2<0:
        e2=e2+a2
    while e3<0:
        e3=e3+a3
    ans=(ans+b1*M//a1*e1)%M
    ans=(ans+b2*M//a2*e2)%M
    ans=(ans+b3*M//a3*e3)%M
    return ans%M


a1=int(input("Please input a1\n"))
a2=int(input("Please input a2\n"))
a3=int(input("Please input a3\n"))
b1=int(input("Please input b1\n"))
b2=int(input("Please input b2\n"))
b3=int(input("Please input b3\n"))

print(CRT(a1,a2,a3,b1,b2,b3))



