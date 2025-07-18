while True:
    try:
        n = int(input("Entrez un entier positif : "))
        if n > 0:
            print(f"✅ Vous avez saisi : {n}")
            break
        else:
            print("❌ Le nombre doit être positif.")
    except ValueError:
        print("❌ Erreur : veuillez entrer un entier valide.")