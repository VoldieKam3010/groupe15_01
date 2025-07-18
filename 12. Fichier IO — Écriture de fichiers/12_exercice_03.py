activite = input("Que voulez-vous enregistrer dans le journal ? : ")

with open("journal.txt", "a", encoding="utf-8") as fichier:
    fichier.write(activite + "\n")

print("✅ Activité ajoutée dans journal.txt")