nom_prenom1 = input("veuillez entrer votre nom puis votre prénom : ")
nom_prenom2 = input("Veuillez entrer votre nom puis vontre prénom : ")

liste_nom_prenom1 = []
liste_nom_prenom1 = nom_prenom1.split()
liste_nom_prenom2 = []
liste_nom_prenom2 = nom_prenom2.split()

if liste_nom_prenom1[0] < liste_nom_prenom2[0]:
    print(liste_nom_prenom1[0].upper(), liste_nom_prenom1 [1].capitalize())
    print(liste_nom_prenom2[0].upper(), liste_nom_prenom2[1].capitalize())
elif liste_nom_prenom1[0] > liste_nom_prenom2[0]:
    print(liste_nom_prenom2[0].upper(), liste_nom_prenom2[1].capitalize())
    print(liste_nom_prenom1[0].upper(), liste_nom_prenom1[1].capitalize())
elif liste_nom_prenom1[1] < liste_nom_prenom2[1]:
    print(liste_nom_prenom1[0].upper(), liste_nom_prenom1[1].capitalize())
    print(liste_nom_prenom2[0].upper(), liste_nom_prenom2[1].capitalize())
elif liste_nom_prenom1 > liste_nom_prenom2:
    print(liste_nom_prenom2[0].upper(), liste_nom_prenom2[1].capitalize())
    print(liste_nom_prenom1[0].upper(), liste_nom_prenom1[1].capitalize())