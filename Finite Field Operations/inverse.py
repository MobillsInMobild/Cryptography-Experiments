import exgcdGF

def inverse(a,m=0b100011011):
    return(exgcdGF.exgcd(a,m)[1])

if __name__ == '__main__':
    a=int(input("Please input your a\n"),16)
    print('%#x'%inverse(a))
