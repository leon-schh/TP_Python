L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

nombre = []
occurence = []
plus_doccurence = 0
for e in L1:
    if e not in nombre:
        nombre.append(e)
        occurence.append(1)
    elif e in nombre:
        position_element_nombre = nombre.index(e)
        occurence[position_element_nombre] += 1
for i in range (len(occurence)):
    if plus_doccurence < occurence[i]:
        plus_doccurence = occurence[i]
        index_occurence = i
print("Le nombre le plus frÃ©quent dans la liste est le : {} ({} fois)".format(nombre[index_occurence],occurence[index_occurence]))
