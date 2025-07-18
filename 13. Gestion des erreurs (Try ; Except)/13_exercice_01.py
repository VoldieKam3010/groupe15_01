try:
    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))
    resultat = a / b
except ZeroDivisionError:
    print("❌ Erreur : division par zéro non applicable.")
else:
    print(f"Résultat : {resultat}")