def VigenereCipherEncode(k,m):
    k=list(k.lower())
    m=list(m.lower())
    c=m
    lenK=len(k)
    lenM=len(m)
    for i in range(lenM):
        c[i]=chr(((ord(m[i])-97)+(ord(k[i%lenK])-97))%26+97)
    return c

def VigenereCipherDecode(k,c):
    k=list(k.lower())
    c=list(c.lower())
    m=c
    lenK=len(k)
    lenC=len(c)
    for i in range(lenC):
        m[i]=chr(((ord(c[i])-97)-(ord(k[i%lenK])-97))%26+97)
    return m


if  __name__ == '__main__':
    k=input("Please input your k\n")
    m=input("Please input your m\n")
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        print("".join(VigenereCipherEncode(k,m)))
    elif(operation=='d'):
        print("".join(VigenereCipherDecode(k,m)))
    else:
        print("Error: Wrong operation\n")

    

