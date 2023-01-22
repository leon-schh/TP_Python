def Monnaie():
    somme = int(input("Entrez une somme d'argent : "))
    input_somme = somme

    b100 = somme // 100
    somme = somme % 100

    b50 = somme // 50
    somme = somme % 50

    b10 = somme // 10
    somme = somme % 10

    p2 = somme // 2
    somme = somme % 2

    p1 = somme

    print(
        f"{input_somme} euros, c'est donc {b100} billets de 100, {b50} de 50, {b10} de 10, {p2} pièces de 2 et {p1} pièce 1.")
Monnaie()
