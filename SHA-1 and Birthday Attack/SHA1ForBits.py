import hashlib


# 循环左移
def leftRotate(word, rotateLength):
    return ((word << rotateLength) | (word >>
                                      (32 - rotateLength))) & 0xffffffff


# 将字符串转换为二进制串
def text2bin(message):
    m = ""
    for char in range(len(message)):
        m += '{0:08b}'.format(ord(message[char]))
    return m


# 填充二进制串
def pad(m):
    temp = m
    m += '1'
    while len(m) % 512 != (512 - 64):
        m += '0'
    m += '{0:064b}'.format(len(temp))
    return m


# 分块
def chunk(m, sizeOfChunk):
    chunks = []
    for i in range(0, len(m), sizeOfChunk):
        chunks.append(m[i:i + sizeOfChunk])
    return chunks


# 扩充，将16组子明文扩充到80组
def extend(smallChunks):
    w = [0] * 80
    # 大端字节序

    for i in range(0, 16):
        w[i] = int(smallChunks[i], 2)

    for i in range(16, 80):
        w[i] = leftRotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
    return w


def SHA1(m):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0


    m = pad(m)

    # 明文分组，每组512位
    bigChunks = chunk(m, 512)

    for eachBigChunks in bigChunks:
        # 子明文分组，每组32位，共16组
        smallChunks = chunk(eachBigChunks, 32)

        w = extend(smallChunks)

        # 初始化
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #main loop:
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (leftRotate(a, 5) + f + e + k + w[i]) & 0xffffffff
            e = d
            d = c
            c = leftRotate(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    hashValue = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    return hashValue


if __name__ == "__main__":
    message = input("Please input your message")
    hashValue = SHA1(message)
    test = hashlib.sha1()
    test.update(message.encode("utf-8"))
    print("MySha1:")
    print(hashValue)
    print("Hashlib's Sha1:")
    print(test.hexdigest())