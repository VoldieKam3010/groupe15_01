mdp = "Python2025"
tentative = ""

while tentative != mdp:
    tentative = input("Entrez le mot de passe : ")
    if tentative != mdp:
        print("Mot de passe incorrect. Réessayez.")

print("✅ Mot de passe correct ! Accès autorisé.")