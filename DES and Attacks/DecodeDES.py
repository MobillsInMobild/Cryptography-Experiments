import HexBinTrans 
import FunctionF
import SubKey 

def decodeDES(m,key):
    m=HexBinTrans.HexToBin(m)
    # 初始置换IP
    message=FunctionF.IP(m,0)
    L=message[0:32]
    R=message[32:64]
    keyList=SubKey.creatKey(key)
    for i in range(16):
        k=keyList[15-i]
        L,R=R,FunctionF.xor(FunctionF.f(R,k),L)
    L,R=R,L
    c=L
    c.extend(R)
    c=FunctionF.IP(c,1)
    c=HexBinTrans.BinToHex(c)
    return c

if __name__=='__main__':
    m=input("Please input your message")
    k=input("Please input your key")
    k=HexBinTrans.HexToBin(k)
    print(decodeDES(m,k))