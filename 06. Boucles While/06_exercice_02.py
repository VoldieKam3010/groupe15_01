choix = -1

while choix != 0:
    print("\n===Menu=== :")
    print("1. Dire bonjour")
    print("2. Additionner deux nombres")
    print("0. Quitter")

    choix = int(input("Choisissez une option : "))

    if choix == 1:
        print("Bonjour ! 👋")
    elif choix == 2:
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        print(f"Somme = {a + b}")
    elif choix == 0:
        print("Au revoir !")
    else:
        print("Choix invalide.")