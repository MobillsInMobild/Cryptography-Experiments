import calculate

def gcd(a,b):
    if b==0b0:
        return a
    else:
        return gcd(b,calculate.mod(a,b))

def exgcd(a,b):
    if b==0b0:
        return [a,0b1,0b0]
    else:
        d,x1,y1=exgcd(b,calculate.mod(a,b))
        x0=y1
        y0=calculate.substract(x1,calculate.multiply(calculate.division(a,b),y1))
        return [d,x0,y0]
if __name__ == '__main__':
    a=int(input("Please input your a\n"),16)
    b=int(input("Please input your b\n"),16)
    print('%#x'%gcd(a,b))
    print([hex(x) for x in exgcd(a,b)])
