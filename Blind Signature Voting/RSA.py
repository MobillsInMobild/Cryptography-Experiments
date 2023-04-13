import exgcd
import Miler_Rabin
import modEx
import random
import math


def RSA_encrypt(m, e, n):
    result = modEx.quick_modEx(m, e, n)
    return result


def RSA_decrypt(m, p, q, n, d):
    # 用于加速运算
    d_Mod_p = d % (p - 1)
    d_Mod_q = d % (q - 1)
    Vp = modEx.quick_modEx(m, d_Mod_p, p)
    Vq = modEx.quick_modEx(m, d_Mod_q, q)
    Xp = q * (exgcd.getInverse(q, p))
    Xq = p * (exgcd.getInverse(p, q))
    #print(Vp*Xp+Vq*Xq)
    result = (Vp * Xp + Vq * Xq) % n


if __name__ == "__main__":
    a = RSA_encrypt(5,573046967,77452180111)
    print(a)
    b= RSA_encrypt(a,1621819703,77452180111)
    print(b)
