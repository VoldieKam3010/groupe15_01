liste_str = input("Entrez une liste d'éléments séparés par des espaces : ")
liste = liste_str.split()

inverse = []
for i in range(len(liste)-1, -1, -1):
    inverse.append(liste[i])

print("Liste inversée :", inverse)