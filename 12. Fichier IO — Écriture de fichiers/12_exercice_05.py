phrase = input("Entrez une phrase : ")

nb_mots = len(phrase.split())
nb_caracteres = len(phrase)

with open("rapport_texte.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"=== Rapport d'analyse ===\n")
    fichier.write(f"Phrase : {phrase}\n")
    fichier.write(f"Nombre de mots : {nb_mots}\n")
    fichier.write(f"Nombre de caractères : {nb_caracteres}\n")

print("✅ Rapport sauvegardé dans 'rapport_texte.txt'.")