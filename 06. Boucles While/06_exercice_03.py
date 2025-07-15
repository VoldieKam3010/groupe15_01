notes = []
print("Entrez vos notes une par une. Tapez -1 pour terminer.")

while True:
    n = float(input("Note : "))
    if n == -1:
        break
    notes.append(n)

if notes:
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne finale : {moyenne:.2f}")
else:
    print("Aucune note saisie.")