texte = input("Entrez un texte : ")

voyelles = "aeiouyAEIOUY"
consonnes = ""

for lettre in texte:
    if lettre.isalpha() and lettre not in voyelles:
        consonnes += lettre

print("Consonnes :", consonnes)