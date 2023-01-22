nombre = float(input("Nombre a multiplier : "))
liste_table = []
nb = 0
for i in range (0,10):
    nb = round(nombre*i,1)
    liste_table.append(nb)
i=0
for e in liste_table:
    print(nombre," * ",i," = ",e)
    i += 1
