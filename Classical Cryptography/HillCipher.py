import exgcd


Alphabet="abcdefghijklmnopqrstuvwxyz"

# 矩阵乘法

def multiplyMatrix(A,B):
    lenA=len(A)
    lenARow=len(A[0])
    lenBRow=len(B[0])
    ans=[]
    # 将ans矩阵置为0矩阵
    cur=[0]*lenBRow
    for i in range(lenA):
        ans.append(cur.copy())
    for i in range(lenA):
        for j in range(lenBRow):
            now=0
            for k in range(lenARow):
                now+=A[i][k]*B[k][j]
            ans[i][j]=now%26
    return ans

# 求矩阵的行列式值

def det(A):
    n=len(A)
    if(n==1):
        return A[0][0]
    ans=0
    for i in range(n):
        new_list=[]
        for a in A:
            new_list.append(a.copy())
        new_list.pop(i)
        for j in range(len(new_list)):
            new_list[j].pop()
        if((i+n)&1==1):
            ans+=det(new_list)*A[i][-1]
        else:
            ans-=det(new_list)*A[i][-1]
    return ans   




# 求矩阵对应的伴随矩阵
def accompany(A):
    n=len(A)
    ans=[]
    cur=[0]*n
    for i in range(n):
        ans.append(cur.copy())
    for i in range(n):
        for j in range(n):
            new=[]
            for a in A:
                new.append(a.copy())
            new.pop(i)
            for k in range(len(new)):
                new[k].pop(j)
            if((i+j)&1==0):
                ans[j][i]=det(new)
            else:
                ans[j][i]=-det(new)
    return ans

# 求矩阵的逆
def reverse(A):
    value=det(A)%26
    if exgcd.gcd(value,26)!=1:
        print("A have no reverse")
        return []
    value_1=exgcd.exgcd(value,26)[1]
    value_1%=26
    cur=accompany(A)
    for i in range(len(A)):
        for j in range(len(A)):
            cur[i][j]*=value_1
            cur[i][j]%=26
    return cur 


def chrToNum(A):
    for i in range(len(A)):
        for j in range(len(A[-1])):
            A[i][j]=int(Alphabet.index(A[i][j]))
    return A


def HillCipherEncode(m,k):
    # 位数不够就补充x
    if(len(m)%len(k)!=0):
        m+="x"*(len(k)-len(m)%len(k))
    lenM=len(m)
    lenK=len(k)
    A=[]
    for i in range(lenM//lenK):
        A.append([])
        for j in range(i*lenK,(i+1)*lenK):
            A[-1].append(Alphabet.index(m[j]))
    ans=multiplyMatrix(A,k)
    c=''
    for i in ans:
        for j in i:
            c+=Alphabet[j]
    return c


def HillCipherDecode(c,k):
    k=reverse(k)
    return HillCipherEncode(c,k)

def HillCipherCrack(m,c):
    m=chrToNum(m)
    c=chrToNum(c)
    print(m)
    print(c)
    m=reverse(m)
    if m==[]:
        return
    else:
        k=multiplyMatrix(m,c)
        return k



if  __name__ == '__main__':
    #k=[[5,8],[17,3]]
    k=[[6,24,1],[13,16,10],[20,17,15]]
    m=input("Please input your m\n")
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        print("".join(HillCipherEncode(m,k)))
    elif(operation=='d'):
        print("".join(HillCipherDecode(m,k)))
    else:
        print("Error: Wrong operation\n")








