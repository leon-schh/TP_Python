nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []
somme_note = 0
for i in range (nombreEtudiants):
    note_entrer = float(input("Note étudiant {} : ".format(i)))
    while (note_entrer < 0) or (note_entrer > 20):
        print("Erreur note interdite")
        note_entrer = float(input("Note étudiant {} : ".format(i)))
    notes.append(note_entrer)
    somme_note += note_entrer

moyenne = round(somme_note/nombreEtudiants,2)
print("Moyenne de la classe : ",moyenne,"\n")
print("Numéro de l'étudiant | note | ecart a la moyenne")
i = 0
for e in notes:
    ecart  = e-moyenne
    ecart = round(ecart,2)
    print("{} | {} | {}".format(i,e,ecart))
    i +=1
