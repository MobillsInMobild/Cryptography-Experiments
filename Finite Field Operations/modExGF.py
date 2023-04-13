import calculate


def modExGF(a,b):
    ans=0b1
    while(b>0):
        if b%2==1:
            ans=calculate.multiply(ans,a)
            b=(b-1)//2
        else:
            b=b//2
        a=calculate.multiply(a,a)
    return ans

if __name__ == '__main__':
    a=int(input("Please input your a\n"),16)
    b=int(input("Please input your b\n"))
    print('%#x'%modExGF(a,b))