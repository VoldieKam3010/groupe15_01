n = int(input("Entrez un nombre : "))

with open("table_multiplication.txt", "w") as fichier:
    for i in range(1, 13):
        fichier.write(f"{n} x {i} = {n * i}\n")

print("✅ Table enregistrée dans table_multiplication.txt")