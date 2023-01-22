import time
nb = int(input("Entrez une valeur de compte a rebours:"))
while nb > 0:
    nb -= 1
    print(nb)
    time.sleep(1)

nb = int(input("Entrez une valeur de compte a rebours (boucle for):"))
i = 0
for i in range(0,nb):
    i += 1
    nb -= 1
    print(nb)
    time.sleep(1)