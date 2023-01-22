"""Exercise a"""
while True:
    s=0
    n=int(input("valleure de n:  "))
    i=0
    for i in range(n+1):
        s=s+i
    print("la somme de tout les entier de 0 à",n, "est",s)
    break

"""Exercise b"""
while True:
    n=int(input("valeur: "))
    if n==100:
        print("ciao")
        break

"""Exercise c"""
while True:
    Y10=0
    Y1015=0
    Y15=0
    for i in range(1, 11):
        x = float(input(f"{i}e valeur: "))
        if x < 0 or x > 20:
            while x < 0 or x > 20:
                print("valleure fausse")
                x = float(input(f"{i}e valeur: "))
            if x < 10:
                Y10 = Y10 + 1
            elif x >= 15:
                Y15 = Y15 + 1
            else:
                Y1015 = Y1015 + 1
        else:
            if x < 10:
                Y10 = Y10 + 1
            elif x >= 15:
                Y15 = Y15 + 1
            else:
                Y1015 = Y1015 + 1
    print("il y a",Y10,"valeurs strictement inferieures à 10",Y1015,"valeurs comprisent entre 10 et 15", Y15, "valeurs strictement superieure à 15")
    break

"""Exercise d"""
while True:
    tmp=0
    total=0
    n=int(input("valeur superieure à 1:  "))
    if n<1:
        n = int(input("valeur SUPERIEURE à 1:  "))
    for i in range(n):
        tmp=tmp+i
        if tmp<=n:
            total=i
        else:
            print(n, "est composé de l'adition des ", total, "permiers entiers")
            break
