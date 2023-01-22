choix = input("for ou while ?:")
n = int(input("Entrer une valeur:"))
i = 0
factoriel = 1
if choix == "while":
    while i < n:
        i += 1
        factoriel = factoriel*i
        print(factoriel)
elif choix == "for":
    for i in range (n):
        i +=1
        factoriel = factoriel * i
        print(factoriel)

print("Le factoriel de n est ",factoriel)