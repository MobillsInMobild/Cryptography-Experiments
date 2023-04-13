def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def exgcd(a,b):
    if b==0:
        return [a,1,0]
    else:
        d,x1,y1=exgcd(b,a%b)
        x0=y1
        y0=x1-a//b*y1
        return [d,x0,y0]


