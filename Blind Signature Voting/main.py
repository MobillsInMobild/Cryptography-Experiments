import CTF
import voter


ctf=CTF.CTF()
alice=voter.voter()

ctf.register()
alice.register(5,ctf.E,ctf.N)
ctf.signE_(alice.e_)
alice.unblind(ctf.e_Signed)
alice.signM()
ctf.receive(alice.e,alice.m,alice.m_,alice.c,alice.n)
#alice.show()
#ctf.show()
ctf.verifyM_(alice.m+1,alice.m_)
ctf.verifye(alice.e-1,alice.c)