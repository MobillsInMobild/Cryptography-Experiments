def _int32(x):
    return int(0xFFFFFFFF & x)


def _int64(x):
    return int(0xFFFFFFFFFFFFFFFF & x)


class MT19937_32:
    # MT19937_32的参数列表如下：
    (w, n, m, r) = (32, 624, 397, 31)
    a = 0x9908B0DF
    f = 1812433253
    (u, d) = (11, 0xFFFFFFFF)
    (s, b) = (7, 0x9D2C5680)
    (t, c) = (15, 0xEFC60000)
    l = 18
    r = 31
    lower_mask = (1 << r) - 1
    upper_mask = _int32(lower_mask)

    # 初始化产生器，seed 作为首项内容
    def __init__(self, seed):
        self.mt = [0] * self.n
        self.mt[0] = seed
        self.mti = 0
        for i in range(1, self.n):
            self.mt[i] = _int32(self.f * (self.mt[i - 1] ^ self.mt[i - 1] >> (self.w-2)) + i)

    def extract_number(self):
        if self.mti == 0:
            self.twist()
        y = self.mt[self.mti]
        y = y ^ y >> self.u
        y = y ^ y << self.s & self.b
        y = y ^ y << self.t & self.c
        y = y ^ y >> self.l
        self.mti = (self.mti + 1) % self.n
        return _int32(y)

    def twist(self):
        for i in range(0, self.n):
            y = _int32((self.mt[i] & self.upper_mask) +
                       (self.mt[(i + 1) % self.n] & self.lower_mask))
            self.mt[i] = (y >> 1) ^ self.mt[(i + self.m) % self.n]

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ self.a

class MT19937_64:
    # MT19937_64的参数列表如下：
    (w, n, m, r) = (64, 312, 156, 31)
    a = 0xB5026F5AA96619E9
    f = 6364136223846793005
    (u, d) = (29, 0x5555555555555555)
    (s, b) = (17, 0x71D67FFFEDA60000)
    (t, c) = (37, 0xFFF7EEE000000000)
    l = 43
    lower_mask = (1 << r) - 1
    upper_mask = _int32(lower_mask)
    # 初始化产生器，seed 作为首项内容
    def __init__(self, seed):
        self.mt = [0] * self.n
        self.mt[0] = seed
        self.mti = 0
        for i in range(1, self.n):
            self.mt[i] = _int64(self.f * (self.mt[i - 1] ^ self.mt[i - 1] >> (self.w-2)) + i)

    def extract_number(self):
        if self.mti == 0:
            self.twist()
        y = self.mt[self.mti]
        y = y ^ y >> self.u
        y = y ^ y << self.s & self.b
        y = y ^ y << self.t & self.c
        y = y ^ y >> self.l
        self.mti = (self.mti + 1) % self.n
        return _int64(y)

    def twist(self):
        for i in range(0, self.n):
            y = _int64((self.mt[i] & self.upper_mask) +
                       (self.mt[(i + 1) % self.n] & self.lower_mask))
            self.mt[i] = (y >> 1) ^ self.mt[(i + self.m) % self.n]

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ self.a

if __name__ == "__main__":
    print(MT19937_32(2).extract_number())
    print(MT19937_64(2).extract_number())
