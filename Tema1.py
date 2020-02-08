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
