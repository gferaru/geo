# Citeste de la tastatura un numar x - afiseaza pe ecran suma cifrelor sale. - daca toate cifrele sale sunt pare,
# afiseaza un mesaj care sa arate asta - afiseaza numarul cifrelor pare si impare ale lui x - afiseaza suma cifrelor
# pare si suma cifrelor impare - afiseaza daca numarul este palindrom* sau nu (palindrom = citind cifrele sale de la
# dreapta la stânga se obţine acelaşi număr ex 12321)

n = int(input("Alege un numar: "))
temp = n
rev = 0
tot = 0
contO = 0
contE = 0
sumO = 0
sumE = 0
while n > 0:
    dig = n % 10
    tot = tot + dig
    n = n // 10
    rev = rev * 10 + dig
    if dig % 2 == 0:
        contE = contE + 1
        sumE = sumE + dig
    elif dig % 2 != 0:
        contO = contO + 1
        sumO = sumO + dig
else:
    print("Numarul cifrelor impare este:", contO)
    print("Numarul cifrelor pare este:", contE)
    print("Suma cifrelor pare este:", sumE)
    print("Suma cifrelor impare este:", sumO)
    print("Suma cifrelor este: ", tot)
    if temp == rev:
        print("Numarul introdus este palindrom!")
    else:
        print("Numarul introdus nu este palindrom!")
