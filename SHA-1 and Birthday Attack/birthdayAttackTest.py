import SHA1ForBits
import random
import SHA1
import birthdayAttack

hashValue=SHA1.SHA1("test")
#print(hashValue)
count=0
num=20
for i in range(num):
    collision=birthdayAttack.birthdayAttack(3,hashValue)
    if collision!=[]:
        count+=1
print(count/num)