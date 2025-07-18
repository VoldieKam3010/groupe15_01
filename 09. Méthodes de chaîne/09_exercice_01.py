texte = input("Entrez un texte : ")

nettoye = texte.strip().lower().replace(".", "!")
print("Texte nettoyé :", nettoye)