entrée = input("Entrez une liste d'éléments séparés par des espaces : ")
liste = entrée.split()

uniques = []
for x in liste:
    if x not in uniques:
        uniques.append(x)

print("Valeurs uniques :", uniques)