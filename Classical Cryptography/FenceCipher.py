import math

def FenceCipherEncode(n,m):
    array=[""]*n
    m=list(m)
    for i in range(len(m)):
        row=i%n
        array[row]+=m[i]

    c=""
    for x in array:
        c+=x
    return c

def FenceCipherDecode(n,c):
    c=list(c)
    array=[""]*n
    if(len(c)%n==0):
        lenRow=len(c)//n
    else:
        lenRow=(len(c)//n)+1
    row=-1
    for i in range(len(c)):
        if(i%lenRow==0):
            row+=1
        array[row]+=c[i]
        #print(array)
    m=""
    for x in range(lenRow):
        for y in range(n):
            if(x+y*lenRow<len(c)):
                m+=array[y][x]
    return m


if  __name__ == '__main__':
    n=int(input("Please input your n\n"))
    m=input("Please input your m\n")
    operation=input("Please input encode(e) or decode(d)\n")
    if(operation=='e'):
        print("".join(FenceCipherEncode(n,m)))
    elif(operation=='d'):
        print("".join(FenceCipherDecode(n,m)))
    else:
        print("Error: Wrong operation\n")








