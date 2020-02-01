import random
j = generated = random.randint(0,100)
i = int(input("Alege_numar: "))
while i != j:
    if i < j:
        print ("Caut un numar mai mare")
    if i > j:
    print ("Caut un numar mai mic")
else:
    print ("Corect!")
