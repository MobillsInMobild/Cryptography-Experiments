import AES
import math


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

# 将任意位数的16进制表示的字符串进行异或


def xor(a, b):
    if len(a) > len(b):
        c = a[:len(b)]
        #print("b:%s,c:%s" % (b, c))
        #print(hex(int(b, 16) ^ int(c, 16))[2:])
        return hex(int(b, 16) ^ int(c, 16))[2:]
    else:
        c = b[:len(a)]
        #print("a:%s,c:%s" % (a, c))
        #print(hex(int(a, 16) ^ int(c, 16))[2:])
        return hex(int(a, 16) ^ int(c, 16))[2:]

# print(xor('0x6e1','0x11'))


# OFB_AES 加密，输入为 message(str)，key(str)
def encryptOFB_AES(message, key, IV):
    m = str_to_hex(message)
    numOfList = math.ceil((len(m)/16))
    o = []
    c = []
    for i in range(numOfList):
        if i == 0:
            o.append(myhex(AES.encrypt(int(IV, 16), int(key, 16))))
        else:
            o.append(myhex(AES.encrypt(int(o[i-1], 16), int(key, 16))))
    for i in range(numOfList):
        if i != numOfList-1:
            plaintext = hexCombine(m[16*i:16*(i+1)])
            #print("plaintext:%s,o[%d]:%s" % (plaintext, i, o[i]))
            c.append(xor(plaintext, o[i]))
        else:
            plaintext = hexCombine(m[16*i:])
            #print("plaintext:%s,o[%d]:%s" % (plaintext, i, o[i]))
            c.append(xor(plaintext, o[i]))

    cipher = "".join(c)
    return cipher


# OFB_AES 解密，输入为 cipher(str)，key(str)
def decryptOFB_AES(cipher, key, IV):
    m = cipher
    numOfList = math.ceil((len(m)/32))
    o = []
    c = []
    for i in range(numOfList):
        if i == 0:
            o.append(myhex(AES.encrypt(int(IV, 16), int(key, 16))))
        else:
            o.append(myhex(AES.encrypt(int(o[i-1], 16), int(key, 16))))
    for i in range(numOfList):
        if i != numOfList-1:
            plaintext = m[32*i:32*(i+1)]
            #print("plaintext:%s,o[%d]:%s" % (plaintext, i, o[i]))
            c.append(xor(plaintext, o[i][2:]))
        else:
            plaintext = m[32*i:]
            #print("plaintext:%s,o[%d]:%s" % (plaintext, i, o[i]))
            c.append(xor(plaintext, o[i][2:]))

    message = "".join(c)
    return hex_to_str(hexSplit(message))


if __name__ == '__main__':
    m = input("Please input your message")
    k = input("Please input your key")
    IV = input("Please input your IV")
    operation = input("Please input encode(e) or decode(d)\n")
    if(operation == 'e'):
        print(encryptOFB_AES(m, k, IV))
    elif(operation == 'd'):
        print(decryptOFB_AES(m, k, IV))
    else:
        print("Error: Wrong operation\n")
