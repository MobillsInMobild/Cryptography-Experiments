def RC4_crypt(message,key):
    sbox=RC4_init(key)
    i=j=0
    c=[]
    for m in message:
        i=(i+1)%256
        j=(j+sbox[i])%256
        sbox[i],sbox[j]=sbox[j],sbox[i]
        t=(sbox[i]+sbox[j])%256
        k=sbox[t]
        c.append(m^k)
    return c

def RC4_init(key):
    keyLen=len(key)
    s=list(range(256))
    t=[]
    for i in range(256):
        t.append(key[i%keyLen])
    j=0
    for i in range(256):
        j=(j+s[i]+t[i])%256
        s[i],s[j]=s[j],s[i]
    return s

if __name__ == "__main__":
    fileName=input("Please input your fileName")
    f=open(fileName,"r",encoding='utf-8')
    m=list(f.read())
    k=list(input("Please input your key"))
    for i in range(len(m)):
        m[i]=ord(m[i])
    for i in range(len(k)):
        k[i]=ord(k[i])
    print(m)
    print(k)
    m=RC4_crypt(m,k)
    for i in range(len(m)):
        m[i]=chr(m[i])
    print(m) 
    result="".join(m)
    print(result)
    f1=open("Out"+fileName,"w",encoding='utf-8')
    f1.write(result)
