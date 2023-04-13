import Miler_Rabin
import random


def getDigitsPrime(digit):
    n = 1
    while Miler_Rabin.Miler_Rabin(n, 10) == False:
        n = random.randint(2**(digit - 1), 2**digit - 1)
    return n


if __name__ == "__main__":
    print(bin(getDigitsPrime(3)))