entrée = input("Entrez une liste d'entiers séparés par des espaces : ")
liste = [int(x) for x in entrée.split()]
somme_pairs = 0
for nb in liste:
    if nb % 2 == 0:
        somme_pairs += nb

print(f"La somme des nombres pairs est : {somme_pairs}")