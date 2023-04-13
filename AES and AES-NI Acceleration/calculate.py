def add(a,b,m=0b100011011):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    return mod(a^b,m)

def substract(a,b,m=0b100011011):
    return add(a,b)

def multiply(a,b,m=0b100011011):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    ans=0
    while b!=0:
        #判断b的最低位是1还是0，如果是1，那么对应ans加上a；反之不加
        if(b&1)!=0:
            ans=add(ans,a)
        #b计算了1位，需要算下一位了，所以对应的a左移一位   
        a=a<<1
        b=b>>1
    return mod(ans,m)

def division(a,b,m=0b100011011):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    ans=0
    x=a.bit_length()-b.bit_length()
    while x>=0:
        #将b移动指相应的位上，然后用a来减，ans在对应位数上变成1
        temp=b<<x
        a=substract(a,temp)
        ans=ans+(1<<x)
        x=a.bit_length()-b.bit_length()
    return mod(ans,m)

def mod(a,b):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    x=a.bit_length()-b.bit_length()
    while x>=0:
        #和division类似，只不过需要求的是剩下来的a
        temp=b<<x
        a=substract(a,temp)
        x=a.bit_length()-b.bit_length()
    return a

if __name__ == '__main__':
    a=int(input("Please input your a\n"),16)
    b=int(input("Please input your b\n"),16)

    op=input("Please input your op\n")
    if op=='+':
        print('%#x'%add(a,b))
    elif op=='-':
        print('%#x'%substract(a,b))
    elif op=='*':
        print('%#x'%multiply(a,b))
    elif op=='/':
        print('%#x'%division(a,b))
    elif op=='%':
        print('%#x'%mod(a,b))
