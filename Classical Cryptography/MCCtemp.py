import MonoalphabeticCipher
Fin=open("Jobs.txt","r")
Fout=open("JobsOutput.txt","w")
m=Fin.read()
Fout.write("".join(MonoalphabeticCipher.MonoalphabeticCipherEncode("abcdefghijklmnopqrstuvwxyz","qwertyuiopasdfghjklzxcvbnm",m)))