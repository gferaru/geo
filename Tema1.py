#Tema: scrieti un program care citeste numere de la tastatura pana ghiceste un numar generat de calculator.
#Pentru aceasta tema, veti avea nevoie de urmatoarele 2 linii de cod:
#             import random
#             generated = random.randint(0,100)
#Despre prima linie nu o sa vorbesc acum, in principiu adaugam functionalitate externa la programul nostru.
#A doua linie genereaza un numar intre 0 si 100.
#Cat timp nu dati de acest numar:
#- daca numarul scris de voi este mai mic decat cel generat, afisati "Caut un numar mai mare"
#- daca numarul scris de voi este mai mare decat cel generat, afisati "Caut un numar mai mic" 
#- daca numarul este egal cu cel generat, afisati "Corect!" si iesiti din instructiunea de while


import random

j = generated = random.randint(0,100)
i = int(input("Alege_numar: "))
while i != j:
    if i < j:
        print ("Caut un numar mai mare")
        i = int(input("Alege_numar: "))
    if i > j:
        print ("Caut un numar mai mic")
        i = int(input("Alege_numar: "))
else:
    print ("Corect!")
