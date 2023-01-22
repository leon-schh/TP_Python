import random
nb_guess = random.randint(0,100)
value = int(input("Deviner la valeur:"))
i=0
while value != nb_guess:
    i += 1
    if value > nb_guess:
        print("Trop grand!")
        value = int(input("Deviner la valeur:"))
    else:
        print("Trop petit!")
        value = int(input("Deviner la valeur:"))

print("Bien Joué le nombre etait bien {} tu a trouver en {} fois".format(nb_guess,i))