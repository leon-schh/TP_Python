eleve1 = {}
eleve1['name'] ='SCHER'
eleve1['firstname'] ='Léon'
eleve1['promo'] ='2022'
eleve1['group'] ='112'

print("Votre nom est {} prénom est {} vous faites partie de la promo {} et votre groupe est {}".format(eleve1['name'],eleve1['firstname'],eleve1['promo'],eleve1['group'],))

print("Les clés du dictionaire sont :")
for e in eleve1.keys():
    print("-",e)
print("Les valeurs du dictionaire sont :")
for e in eleve1.values():
    print("-",e)
print("Les tuplet du dictionaire sont :")
for e in eleve1.items():
    print("-",e)

eleve2 = {}
eleve2['name'] ='toto'
eleve2['firstname'] ='titi'
eleve2['promo'] ='2022'
eleve2['group'] ='202'

binome = {}
binome['PC14'] = eleve1
binome['PC15'] = eleve2

print("Les étudiants formant le binome sont :")
print("L'étudiant",binome['PC14']['name'],binome['PC14']['firstname'],"du groupe",binome['PC14']['group'])
print("L'étudiant",binome['PC15']['name'],binome['PC15']['firstname'],"du groupe",binome['PC15']['group'])
