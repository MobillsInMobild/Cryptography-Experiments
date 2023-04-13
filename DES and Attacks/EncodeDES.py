import HexBinTrans 
import FunctionF
import SubKey 

def encodeDES(m,key):
    m=HexBinTrans.HexToBin(m)
    # 初始置换IP
    message=FunctionF.IP(m,0)
    L=message[0:32]
    R=message[32:64]
    keyList=SubKey.creatKey(key)
    #print(keyList)
    for i in range(16):
        k=keyList[i]
        L,R=R,FunctionF.xor(FunctionF.f(R,k),L)
        # print("L_%d:"%i)
        # print(HexBinTrans.BinToHex(L))
        # print("R_%d:"%i)
        # print(HexBinTrans.BinToHex(R))
    L,R=R,L
    p=L
    p.extend(R)
    p=FunctionF.IP(p,1)
    p=HexBinTrans.BinToHex(p)
    return p



if __name__=='__main__':
    m=input("Please input your message")
    k=input("Please input your key")
    k=HexBinTrans.HexToBin(k)
    #m="0x02468aceeca86420"
    #k="0x0f1571c947d9e859"
    print(encodeDES(m,k))