import EncodeDES
import DecodeDES
import HexBinTrans
def encode3DES(p,k1,k2,k3):
    return EncodeDES.encodeDES(DecodeDES.decodeDES(EncodeDES.encodeDES(p,k1),k2),k3)

if __name__=='__main__':
    m=input("Please input your message")
    k=input("Please input your k")
    k=HexBinTrans.HexToBin(k)
    k1=k[0:len(k)//2]
    k2=k[len(k)//2:len(k)]
    k3=k1
    print(encode3DES(m,k1,k2,k3))