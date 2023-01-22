fin = False
while fin == False :
    h_debut = int(input("Donnez l’heure de début de la location (un entier) :"))
    h_fin = int(input("Donnez l’heure de fin de la location (un entier) :"))
    tarif_1 =0
    tarif_2 =0
    i = h_debut
    if h_debut < 0 or h_fin > 24 :
        print("Les heures doivent être comprises entre 0 et 24 !\n")
    elif h_debut == h_fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    elif h_fin < h_debut:
        print("Attention ! le début de la location est après la fin ... \n")
    else:
        for i in range(h_debut,h_fin):
            if (0<=i and i<=6) or (17<=i and i<=24):
                tarif_1 += 1
                i += 1
            elif (6<i and i<17):
                tarif_2 += 1
                i += 1
        total = tarif_1 + tarif_2*2
        print("Vous avez loué votre vélo pendant")
        if tarif_1 != 0:
            print(tarif_1," heure(s) au tarif horaire de 1.0 euro(s)")
        if tarif_2 != 0:
            print(tarif_2," heure(s) au tarif horaire de 2.0 euro(s)")
        print("Le montant total à payer est de ",total," euro (s).")
        fin = True
