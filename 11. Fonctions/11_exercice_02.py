def stats(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    maximum = max(liste)
    return somme, moyenne, maximum

nombres = [float(x) for x in input("Entrez une liste de nombres : ").split()]

somme, moyenne, maximum = stats(nombres)
print(f"Somme : {somme}, Moyenne : {moyenne:.2f}, Max : {maximum}")