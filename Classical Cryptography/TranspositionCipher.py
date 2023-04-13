import copy
# 横着放，竖着拿
def TranspositionCipherEncode(m,k):
    # 位数不够就补充x
    if(len(m)%len(k)!=0):
        m+="x"*(len(k)-len(m)%len(k))
    c=[]
    numRow=len(m)//len(k)
    numColumn=len(k)
    ans=[]
    # 创建一个空矩阵
    cur=['a']*numColumn
    for i in range(numRow):
        ans.append(cur.copy())
    # 从左往右，从上到下，填充矩阵
    for i in range(numRow):
        for j in range(numColumn):
            ans[i][j]=m[i*numColumn+j]
    #print(ans)
    #读取矩阵，根据密钥对应的值读取对应的列
    for i in range(numColumn):
        for j in range(numRow):
            c.append(ans[j][k.index(i+1)])
    return c


def TranspostionCipherDecode(c,k):
    m=[]
    numRow=len(c)//len(k)
    numColumn=len(k)
    ans=[]
    # 创建空矩阵
    cur=['a']*numColumn
    for i in range(numRow):
        ans.append(cur.copy())
    now=copy.deepcopy(ans)
    # 从密文从上到下，从左往右，填充矩阵
    for i in range(numColumn):
        for j in range(numRow):
            ans[j][i]=c[j+i*numRow]

    # 根据密钥调整各列之间的位置
    for i in range(numColumn):
        for j in range(numRow):
            now[j][k.index(i+1)]=copy.deepcopy(ans)[j][i]
    
    #从左往右，从上到下，输出明文
    for i  in range(numRow):
        for j in range(numColumn):
            m.append(now[i][j])
    return m


k=[7,3,4,5,2,6,1]
m="obestdnfhhmoeaaohleywsdloreb"


print(TranspositionCipherEncode(m,k))
#print(TranspostionCipherDecode(TranspositionCipherEncode(m,k),k))