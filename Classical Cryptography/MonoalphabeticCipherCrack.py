import MonoalphabeticCipher

class timesLettes:
    totel=0
    def __init__(self,letter):
        self.letter=letter
        self.times=0

    def timesPlus(self):
        self.times+=1
        self.totel+=1

    def getLetter(self):
        return self.letter

    def getTimes(self):
        return self.times
    
    def getTotel(self):
        return self.totel



def MonoalphabeticCipherCrack(m):
    alphabet=[]
    listAlpha=[]
    for i in range(ord('a'),ord('z')+1):
        alphabet.append(timesLettes(chr(i)))
    for i in m:
        alphabet[ord(i)-ord('a')].timesPlus()
    for i in range(len(alphabet)):
        for j in range(0,len(alphabet)-1-i):
            if alphabet[j].getTimes()<alphabet[j+1].getTimes():
                alphabet[j],alphabet[j+1]=alphabet[j+1],alphabet[j]
    for i in range(len(alphabet)):
        listAlpha.append(alphabet[i].getLetter())
        print("%c:%d"%(alphabet[i].getLetter(),alphabet[i].getTimes()))
    return MonoalphabeticCipher.MonoalphabeticCipherDecode("etaoinshrdlcumwfgypbvkjxqz",listAlpha,m)



fin=open("JobsOutput.txt","r")
fout=open("OutputForMPCC.txt","w")
m=fin.read().lower()
fout.write("".join(MonoalphabeticCipherCrack(m)))
