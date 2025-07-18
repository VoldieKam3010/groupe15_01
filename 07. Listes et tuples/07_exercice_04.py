etudiants = []
nb = int(input("Combien d'étudiants ? : "))

for _ in range(nb):
    nom = input("Nom de l'étudiant : ")
    note = float(input("Note : "))
    etudiants.append((nom, note))

print("Étudiants avec note >= 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"{nom} : {note}")