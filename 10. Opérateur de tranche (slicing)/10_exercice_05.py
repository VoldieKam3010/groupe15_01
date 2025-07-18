liste = input("Entrez une liste de nombres séparés par des espaces : ").split()

elements_pairs = liste[::2]  # prend uniquement les indices pairs
print("Éléments aux indices pairs :", elements_pairs)