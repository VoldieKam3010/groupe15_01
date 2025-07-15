carres = []
for i in range(1, 21):
    carres.append(i ** 2)

print("Tous les carrés :", carres)

print("Carrés supérieurs à 100 :")
for c in carres:
    if c > 100:
        print(c)