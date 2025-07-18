notes = [float(x) for x in input("Entrez une liste de notes séparées par des espaces : ").split()]
moyenne = sum(notes) / len(notes)

with open("statistiques.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"Nombre de notes : {notes}\n")
    fichier.write(f"Moyenne : {moyenne:.2f}\n")

print("✅ Statistiques sauvegardées dans 'statistiques.txt'.")