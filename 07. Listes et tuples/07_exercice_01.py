entree = input("Entrez une liste de nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

n = len(liste)
for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            # échange
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print("Liste triée :", liste)