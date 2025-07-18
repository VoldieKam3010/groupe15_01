entrée = input("Entrez une liste de nombres séparés par des espaces : ")
nombres = [float(x) for x in entrée.split()]

maximum = max(nombres)
minimum = min(nombres)
moyenne = sum(nombres) / len(nombres)

print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne:.2f}")