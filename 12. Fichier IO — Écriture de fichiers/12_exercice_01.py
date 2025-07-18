with open("utilisateurs.txt", "w") as fichier:
    while True:
        nom = input("Entrez un nom d'utilisateur (ou stop pour finir) : ")
        if nom.lower() == "stop":
            break
        fichier.write(nom + "\n")

print("✅ Noms enregistrés dans utilisateurs.txt")