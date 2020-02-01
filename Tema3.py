def functie(x):
    if x % 2 == 0:
        var = int (x * (x + 2) / 4)
    if x < 10 or x > 20:
        print(x)
for x in range(0,100):
    functie(x)