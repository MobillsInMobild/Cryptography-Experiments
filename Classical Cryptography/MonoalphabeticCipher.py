def MonoalphabeticCipherEncode(a,b,m):
    a=list(a)
    b=list(b)
    m=list(m.lower())
    c=m
    for i in range(len(m)):
        c[i]=b[a.index(m[i])]

    return c

def MonoalphabeticCipherDecode(a,b,c):
    a=list(a)
    b=list(b)
    c=list(c.lower())
    m=c
    for i in range(len(c)):
         m[i]=a[b.index(c[i])]

    return m

if  __name__ == '__main__':
    a=input("Please input your a\n")
    b=input("Please input your b\n")
    m=input("Please input your m\n")
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        print("".join(MonoalphabeticCipherEncode(a,b,m)))
    elif(operation=='d'):
        print("".join(MonoalphabeticCipherDecode(a,b,m)))
    else:
        print("Error: Wrong operation\n")