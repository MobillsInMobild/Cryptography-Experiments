def VernamCipherEncode(k,m):
    k=list(k.lower())
    m=list(m)
    c=m
    lenK=len(k)
    lenM=len(m)
    for i in range(lenM):
        c[i]=chr(((ord(m[i]))^(ord(k[i%lenK]))))
    return c

def VernamCipherDecode(k,c):
    k=list(k.lower())
    c=list(c)
    m=c
    lenK=len(k)
    lenC=len(c)
    for i in range(lenC):
        m[i]=chr(((ord(c[i]))^(ord(k[i%lenK]))))
    return m 

if  __name__ == '__main__':
    k=input("Please input your k\n")
    Fin=input("Please input your Fin\n")
    Fout=input("Please input your Fout\n")
    F=open(Fin,'r')
    F_=open(Fout,'w')
    m=F.read()
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        F_.write("".join(VernamCipherEncode(k,m)))
    elif(operation=='d'):
        F_.write("".join(VernamCipherDecode(k,m)))
    else:
        print("Error: Wrong operation\n")
