import EncodeDES
import DecodeDES
import HexBinTrans
def decode3DES(p,k1,k2,k3):
    return DecodeDES.decodeDES(EncodeDES.encodeDES(DecodeDES.decodeDES(p,k3),k2),k1)

if __name__=='__main__':
    m=input("Please input your message")
    k=input("Please input your k")
    k=HexBinTrans.HexToBin(k)
    k1=k[0:len(k)//2]
    k2=k[len(k)//2:len(k)]
    k3=k1
    print(decode3DES(m,k1,k2,k3))