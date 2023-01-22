taille_vecteur = int(input("Quelle est la taille de vos vecteur [entre 1 et 10] ? "))
v1 = []
v2 = []
print("Saisie du premier vecteur :")
for i in range (taille_vecteur):
    v1.append(float(input("v1[{}] = ".format(i))))

print("Saisie du second vecteur :")
for i in range(taille_vecteur):
    v2.append(float(input("v2[{}] = ".format(i))))

produit = 0
somme = 0
for i in range(taille_vecteur):
    produit = v1[i]*v2[i]
    somme += produit

print("Le produit scalaire de v1 par v2 vaut ",somme)
