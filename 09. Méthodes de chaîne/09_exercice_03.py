texte = input("Entrez un texte : ").lower()
mot = input("Mot à chercher : ").lower()

occurrences = texte.count(mot)
print(f"Le mot '{mot}' apparaît {occurrences} fois.")