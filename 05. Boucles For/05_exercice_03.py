texte = input("Entrez une chaîne : ")

inverse = ""
for c in texte:
    inverse = c + inverse  # ajoute le caractère au début

print(f"Chaîne inversée : {inverse}")