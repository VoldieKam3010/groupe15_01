n = int(input("Entrez un nombre n pour sa table de multiplication : "))

print(f"Table de multiplication de {n} :")
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")