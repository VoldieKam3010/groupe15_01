mots = input("Entrez une liste de mots séparés par des espaces : ").split()

voyelles = "aeiouyAEIOUY"
compteur = 0

for mot in mots:
    for lettre in mot:
        if lettre in voyelles:
            compteur += 1

print(f"Nombre total de voyelles : {compteur}")