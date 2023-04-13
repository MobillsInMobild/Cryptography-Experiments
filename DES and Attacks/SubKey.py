MaxTime = 16
# 生成子密钥的置换表1，将64位的密钥转换为56位
PC_1=[ 57, 49, 41, 33, 25, 17,  9,
              1, 58, 50, 42, 34, 26, 18,
             10,  2, 59, 51, 43, 35, 27,
             19, 11,  3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
             14,  6, 61, 53, 45, 37, 29,
             21, 13,  5, 28, 20, 12,  4 ]


# 生成子密钥的置换表2，将56位的密钥转换为48位
PC_2=[ 14, 17, 11, 24,  1,  5,
              3, 28, 15,  6, 21, 10,
             23, 19, 12,  4, 26,  8,
             16,  7, 27, 20, 13,  2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32 ]

# 切片法，将列表中的元素循环左移step
def ListMove(l,step):
    return l[step:]+l[:step]

def creatKey(key):
    keyList=[]
    key56=[0 for i in range(len(PC_1))]

    # 置换选择 PC_1
    for i in range(len(PC_1)):
        key56[i]=key[PC_1[i]-1]

    # 生成16个密钥
    for i in range(16):

        #密钥的循环左移
        key48=[0 for j in range(48)]
        # 确定每轮左移的 step
        if(i==0 or i ==1 or i==8 or i==15):
            step=1
        else:
            step=2
        # 分成两组
        key56L=key56[0:28]
        key56R=key56[28:56]
        # 循环左移
        key56L=ListMove(key56L,step)
        key56R=ListMove(key56R,step)
        # 连接
        key56=key56L+key56R
        
        # 置换选择PC_2
        for j in range(len(PC_2)):
            key48[j]=key56[PC_2[j]-1]

        # 将所得密钥加入到密钥集中
        keyList.append(key48)
    
    return keyList

