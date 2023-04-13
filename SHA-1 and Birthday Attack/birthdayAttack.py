import SHA1ForBits
import random
import SHA1

def birthdayAttack(n,m):
    m=m[:n]
    collision = []
    for i in range(0,2**(4*n-1)):
        t = random.randint (2**16, 2**64)
        src = bin(t)[2:]
        cur_hash = SHA1ForBits.SHA1(src)
        if cur_hash[:n]==m :
            collision.append((src,cur_hash))
    return collision

if __name__ == "__main__":
    hashValue=SHA1.SHA1("test")
    print(hashValue)
    collision=birthdayAttack(3,hashValue)
    for i in collision:
        print(i)