import SDES

import random


def TestDES(m,k1,k2):
    return SDES.encrypt(SDES.encrypt(m,k1),k2)



def crack_middle(m,c,trueKey1,trueKey2):
    middle=[]
    keyList=[]
    # 生成 keyList
    for i in range(2048):
        i=bin(i)
        #print(i)
        i=i[2:]
        i="0000000000"+i
        i=i[-10:-1]+i[-1]
        keyList.append(i)
    #生成 k1 加密之后的密文
    for k1 in keyList:
        middle.append(SDES.encrypt(m,k1))
    #生成 k2 解密之后的明文
    for k2 in keyList:
        cur=SDES.decrypt(c,k2)
        # 如果所得明文和密文有竞合
        if cur in middle:
            k1List=[]
            for i in range(len(middle)):
                if middle[i]==cur:
                    k1List.append(i)
            for i in range(len(k1List)):
                k1=keyList[k1List[i]]
                # 检验可行的解
                flag=0
                for j in range(50):
                    p = ""
                    for k in range(8):
                        p=p+(random.choice("01") )
                    #print("%s,%s\n"%(k1,k2))
                    cipher=TestDES(p,trueKey1,trueKey2)
                    if cipher!=TestDES(p,k1,k2):
                        flag=1
                        break
                if flag==0:
                    return k1,k2 

if __name__=='__main__':
    m='11101010'
    k1='0011111010'
    k2='1111111100'
    c=TestDES(m,k1,k2)
    #print(c)
    #print(SDES.encrypt(m,k1))
    #print(SDES.decrypt(c,k2))
    print(crack_middle(m,c,k1,k2))



