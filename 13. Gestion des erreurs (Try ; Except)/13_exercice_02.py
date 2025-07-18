texte = input("Entrez un texte : ")

try:
    entier = int(texte)
except ValueError:
    print("❌ Erreur : ce texte ne peut pas être converti en entier.")
else:
    print(f"Conversion réussie : {entier}")