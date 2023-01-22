def Notes():
    notes = []
    coefs = []

    for i in range(5):
        user_input = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ")
        note, coef = user_input.split(" ")
        notes.append(float(note))
        coefs.append(int(coef))

    moyenne = sum([notes[i] * coefs[i] for i in range(5)]) / sum(coefs)

    if moyenne > 10 and all(note >= 8 for note in notes):
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")
