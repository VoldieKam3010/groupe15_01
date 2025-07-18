elements = input("Entrez une liste d'éléments séparés par des espaces : ").split()

for index, valeur in enumerate(elements):
    print(f"Indice {index} : {valeur}")