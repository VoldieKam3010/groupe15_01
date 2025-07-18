fichier_nom = input("Nom du fichier à ouvrir : ")

try:
    with open(fichier_nom, "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("❌ Erreur : fichier introuvable.")
else:
    print("Contenu du fichier :")
    print(contenu)