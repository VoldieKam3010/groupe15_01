age = int(input("Entrez votre âge : "))
situation = input("Situation (étudiant, salarié, retraité) : ").strip().lower()

if age < 18:
    tarif = 5
elif 18 <= age <= 25:
    if situation == "étudiant":
        tarif = 6
    else:
        tarif = 8
else:  # plus de 25 ans
    if situation == "retraité":
        tarif = 7
    else:
        tarif = 10

print(f"Le tarif est de {tarif} €")