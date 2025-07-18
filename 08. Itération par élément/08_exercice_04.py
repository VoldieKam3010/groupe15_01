phrase = input("Entrez une phrase : ")
mots = phrase.split()

compteur = 0
for mot in mots:
    if len(mot) > 5:
        compteur += 1

print(f"Nombre de mots de plus de 5 lettres : {compteur}")