date = (input("entrer votre date : "))
while len(date) != 8 :
    date = (input("Erreur de format entrer votre date : "))
jour = ""
mois = ""
annee = ""
bisexstile = False
pair_impair = False
fevrier = False
i = 0
for e in date:
    if i < 2:
        jour += e
        i += 1
    elif (i > 1) and (i < 4):
        mois += e
        i += 1
    elif i > 3 :
        annee += e
        i += 1

jour = int(jour)
mois = int(mois)
annee = int(annee)

if ((annee%4 == 0) and (annee%100 != 0)) or (annee%400 == 0):
    bisexstile = True

if ((mois == 1)or(mois == 3)or(mois == 5)or(mois == 7)or(mois == 8)or(mois == 10)or(mois == 12)) and (mois <=12) and (mois > 0) and (mois != 2):
    pair_impair = True
elif mois > 12 or mois < 0:
    raise print("Erreur le mois n'existe pas")
elif mois == 2:
    fevrier = True


if jour < 32 and jour > 0:
    if (pair_impair == True) and (jour == 31):
        raise print("Erreur le jour n'existe pas")
    elif (fevrier== True) and (bisexstile == False) and (jour > 28):
        raise print("Erreur février non bisextile ne contient que 28 jours ")
    elif (fevrier== True) and (bisexstile == True) and (jour > 29):
        raise print("Erreur février bisextile ne contient que 29 jours ")
else:
    raise print("Erreur le jour n'existe pas")

print("La date est valide")
