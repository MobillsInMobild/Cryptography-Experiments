import exgcd 

def AffineCipherEncode(m,k,p):
    m=list(m.lower())
    c=m
    if(exgcd.gcd(k,26)!=1):
        print("Error: k isn't co-prime with 26\n")
        return []
    for i in range(len(m)):
        c[i]=chr(((ord(m[i])-97)*k+p)%26+97)
    return c

def AffineCipherDecode(c,k,p):
    c=list(c.lower())
    m=c
    if(exgcd.gcd(k,26)!=1):
        print("Error: k isn't co-prime with 26\n")
        return []
    else:
        k_=(exgcd.exgcd(k,26)[1]+26)%26

    for i in range(len(c)):
        m[i]=chr((((ord(c[i])-97)-p)*k_)%26+97)
    return m








if  __name__ == '__main__':
    m=input("Please input your m\n")
    k=int(input("Please input your k\n"))
    p=int(input("Please input your p\n"))
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        print("".join(AffineCipherEncode(m,k,p)))
    elif(operation=='d'):
        print("".join(AffineCipherDecode(m,k,p)))
    else:
        print("Error: Wrong operation\n")