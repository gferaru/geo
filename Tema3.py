'''
Citeste de la tastatura numere pana se
citeste valoarea 0. apoi:
- Sa se afiseze cel mai mare numar citit de la tastatura 
- Sa se afiseze suma numerelor impare citite
- Sa se afiseze numarul maxim de numere citite consecutiv crescator 
(exemplu:
1 2 3 0 -> 3 numere (1 2 3)
1 2 0 3 4 5 -> 3 numere (3 4 5)
5 3 2 0 -> 0 numere 
5 3 1 2 -> 2 numere (1 2)
)
'''

lista = []
sumO = 0
contc = 1
contm = 0
while True:
	n = int(input("Alege un numar: "))
	lista.append(n)
	if n % 2 != 0:
		sumO = sumO + n
	if n == 0:
		print("Numarul maxim din lista este:", max(lista))
		print("Suma numerelor impare este: " , sumO)
		sumO = 0
		for i in range(len(lista) - 1):
			if lista[i] + 1 == lista[i + 1]:
				contc = contc + 1
				contm = contc
		else:
				print("Numere consecutive: " , contm)
				print(lista)
				contc = 1
				contm = 0
				lista.clear()