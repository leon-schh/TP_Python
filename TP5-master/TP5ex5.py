def FicheDePaye():
    heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = float(input("Entrez le salaire horaire : "))

    salaire_base = heures_travaillees * salaire_horaire

    if heures_travaillees > 200:
        salaire_supplementaire = (heures_travaillees - 200) * (salaire_horaire * 0.5) + (40 * salaire_horaire * 0.25)
    elif heures_travaillees > 160:
        salaire_supplementaire = (heures_travaillees - 160) * (salaire_horaire * 0.25)
    else:
        salaire_supplementaire = 0

    salaire_total = salaire_base + salaire_supplementaire
    print(f"Le salaire total est de {salaire_total} euros.")
FicheDePaye()
