def add(a,b):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    return a^b

def substract(a,b):
    return add(a,b)

def multiply(a,b):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    ans=0
    while b!=0:
        #判断b的最低位是1还是0，如果是1，那么对应ans加上a；反之不加
        if(b&1)!=0:
            ans=add(ans,a)
        #b计算了1位，需要算下一位了，所以对应的a左移一位   
        a=a<<1
        b=b>>1
    return ans

def division(a,b):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    ans=0
    x=a.bit_length()-b.bit_length()
    while x>=0:
        #将b移动指相应的位上，然后用a来减，ans在对应位数上变成1
        temp=b<<x
        a=substract(a,temp)
        ans=ans+(1<<x)
        x=a.bit_length()-b.bit_length()
    return ans

def mod(a,b):
    if(a<0):
        a=add(~a,1)
    if(b<0):
        b=add(~b,1)
    x=a.bit_length()-b.bit_length()
    while x>=0:
        #和division类似，只不过需要求的是剩下来的a
        temp=b<<x
        a=substract(a,temp)
        x=a.bit_length()-b.bit_length()
    return a


def isRec(num,n=8):
    index=1<<(n//2+1)
    flag=False
    for j in range(2,index,2): 
        if mod(num,j)==0: 
            flag=True
            break
    return flag

def polynomial(n=8):
    k=2**n-1 
    lhs=(1<<n)+1
    rhs=1<<(n+1)

    for num in range(lhs,rhs,2):
        flag=False
        t=(1<<k)+1
        #print((num))
        if isRec(num)==False:
           # print(num)
            if mod(t,num)==0:
                #print('AA')
                flag=True
                for i in range(k):
                    t=(1<<i)+1
                    #print("t:%d"%t)
                    if mod(t,num)==0:
                       # print("t:%d,num:%d"%(t,num))
                        flag=False
                        break
        if flag==True:
            print(bin(num))
    return 

if __name__ == '__main__':
    polynomial()