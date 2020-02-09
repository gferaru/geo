#Scrieti o functie care se foloseste de for sa parcurga numerele de la 0 la 100.
#Daca numarul este par, va fi adunat intr-o alta variabila, si se va trece la urmatorul numar.
#Daca numarul este mai mic decat 10, va fi afisat pe ecran.
#Daca numarul este intre 10 si 20, vom trece la urmatorul numar.

def f(k):
    if k % 2 == 0:
        var = int (x * (x + 2) / 4)
#       print(var)       
    if k < 10 or k > 20:
        print(k)
        
        
for x in range(0,100):
    f(x)
