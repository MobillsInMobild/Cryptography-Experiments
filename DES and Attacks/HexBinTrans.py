
# 0~15整数转bit
def intTobit(n):
    a=[]
    for i in range(4):
        a.insert(0,str(n%2))
        n=int(n/2)
    return a

# 16进制转2进制比特串
def HexToBin(text):
    result=[]
    for i in range(2,len(text)):
        result.extend(intTobit(int(text[i],16)))
    return result

# 2进制比特串转16进制
def BinToHex(text):
    result=[]
    q=len(text)//4
    for i in range(q):
        temp=int(text[4*i])*8 + int(text[4*i+1])*4 + int(text[4*i+2])*2 + int(text[4*i+3])*1
        #最前2位是0x
        result.extend(hex(temp)[2:].lower())
    rs="".join(result)
    rs="0x"+rs
    return rs

# 单元测试
if __name__ == '__main__':
    print(intTobit(1))
    print(HexToBin("0f1571c947d9e859"))
    print(BinToHex(HexToBin("0f1571c947d9e859")))