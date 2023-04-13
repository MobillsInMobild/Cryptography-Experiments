from SHA1ForBits import SHA1 as SHA1
import hmac

def text2bin(message):
    m = ""
    for char in range(len(message)):
        m += '{0:08b}'.format(ord(message[char]))
    return m


def pad(k, b):
    while len(k) % b != 0:
        k = k+"0"
    return k

def xor(a,b):
    a=list(a)
    b=list(b)
    if len(a)!=len(b):
        print("Error")
        return
    else:
        c=["0"]*len(a)
        for i in range(len(a)):
            c[i]=str(int(a[i])^int(b[i]))
    return "".join(c)

def hex2bin(m):
    result=""
    for char in m:
        result+="{0:04b}".format(int(char,16))
    return result

def HMACSHA1(message, key):  #密钥，原始消息
    b = 512
    blockSize = 64
    ipad = "00110110" * (b // 8)
    opad = "01011100" * (b // 8)
    m = text2bin(message)
    k = text2bin(key)

    if (len(k) > blockSize):
        k = SHA1(k)

    if (len(k) < blockSize):
        k = pad(k, b)

    #print(k)
    content1 = xor(k,ipad) + m
    #print(m)
    h1 = SHA1(content1)
    #print(h1)
    content2 = xor(k,opad) + hex2bin(h1)
    #print(hex2bin(h1))
    h2 = SHA1(content2)
    ans = h2
    return ans


if __name__ == "__main__":
    #message = input("Please input your message")
    #key=input("Please input your key")
    key = "key"
    message = "The quick brown fox jumps over the lazy dog"
    HMACValue = HMACSHA1(message, key)
    print(HMACValue)