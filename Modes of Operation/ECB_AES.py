import AES


def myhex(i):
    return "0x"+"{:0>32x}".format(i)

# 字符串转16进制列表


def str_to_hex(s):
    hexList = []
    for i in s:
        hexList.append(hex(ord(i)))
    # print(hexList)
    return(hexList)


# 16进制字符串转字符串
def hex_to_str(hexList):
    s = []
    t = ""
    for i in hexList:
        s.append(chr(int(i, 16)))
    t = t.join(s)
    return t


# 字符串填充
def fillChr(hexList):
    size = len(hexList)
    r = size % 16
    for i in range(16-r):
        hexList.append(hex(16-r))
    return hexList


# 将16进制的list拼接成一个32字节的字符串
def hexCombine(hexList):
    plaintext = "0x"
    for i in hexList:
        if(len(i) == 3):
            plaintext = plaintext+"0"+i[2]
        elif(len(i) == 4):
            plaintext = plaintext+i[2:]
        else:
            print("Error:hexList,size=%d" % len(i))
    return plaintext

# 将一个32字节的字符串分解成一个16进制的list


def hexSplit(s):
    hexList = []
    for i in range(0, len(s), 2):
        temp = s[i:i+2]
        hexList.append(temp)
    return hexList


# ECB_AES 加密，输入为 message(str)，key(str)
def encryptECB_AES(message, key):
    m = fillChr(str_to_hex(message))
    numOfList = len(m)//16
    c = []
    for i in range(numOfList):
        plaintext = hexCombine(m[16*i:16*(i+1)])
        # print(plaintext)
        # print(key)
        c.append(myhex(AES.encrypt(int(plaintext, 16), int(key, 16))))
    for i in range(len(c)):
        c[i] = c[i][2:]
    cipher = "".join(c)
    return cipher


# ECB_AES 解密，输入为 cipher(str)，key(str)
def decryptECB_AES(cipher, key):
    numOfList = len(cipher)//32
    m = []
    # 将字符串分组
    for i in range(numOfList):
        m.append(cipher[i*32:(i+1)*32])
    # print(m)
    # 对每组字符串进行 AES 解密
    for i in range(len(m)):
        m[i] = myhex(AES.decrypt(int(m[i], 16), int(key, 16)))
    # print(m)
    # 将解密后的字符串转换为hexList
    for i in range(len(m)):
        m[i] = hexSplit(m[i][2:])
    # print(m)
    # 删除填充
    fullNum = int(m[-1][-1], 16)
    for i in range(fullNum):
        m[-1].pop()
    # print(m)
    # 将hexList转换为字符串
    for i in range(len(m)):
        m[i] = hex_to_str(m[i])
    message = "".join(m)
    return message



if __name__ == '__main__':
    m = input("Please input your message")
    k = input("Please input your key")
    operation = input("Please input encode(e) or decode(d)\n")
    if(operation == 'e'):
        print(encryptECB_AES(m, k))
    elif(operation == 'd'):
        print(decryptECB_AES(m, k))
    else:
        print("Error: Wrong operation\n")
