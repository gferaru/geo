#Scrieti o functie care afiseaza pe ecran numerele de la 1 la 100, fiecare pe un rand.
#Daca numarul este multiplu de 3, afisati "Fizz" in loc de acel numar.
#Daca numarul este multiplu de 5, afisati "Buzz" in loc de acel numar.
#Daca numarul este multiplu si de 3 si de 5, afisati "FizzBuzz" in loc de acel numar.

def f(k):
    if k % 3 == 0 and k % 5 == 0:
        print("FizzBuzz")
    elif k % 3 == 0:
        print("Fizz")
    elif k % 5 == 0:
        print("Buzz")
    else:
        print(k)


for x in range(1, 101):
    f(x)
