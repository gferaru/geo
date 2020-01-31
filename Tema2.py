n = int(input("Alege un numar: "))
temp = n
rev = 0
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
    rev = rev*10+dig
    print(type(rev))
    rev1 = str(rev)
    print(type(rev1))
print("Suma cifrelor este: ", tot)
if temp == rev1:
	print("Numarul introdus este palindrom!")
else:
	print("Numarul introdus nu este palindrom!")
#if dig %2 == 0:
#	print("Toate cifrele sunt pare")
#else:
#	print("Nu toate cifrele sunt pare")
#b = []
#b.append(n)
#digE = 0
#digO = 0
#for j in b:
#	if j > 0:
#		digE = digE + j
#	else:
#		digO = digO + j
#	print("Numarul cifrelor pare este:" , digE , "Numarul cifrelor impare este:" , digO)