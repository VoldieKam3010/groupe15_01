#Vérification de la température
temp = float(input("Température en °C : "))

#Conseils en fonction de la température
if temp >= 35:
    print("Très chaud, restez hydraté.")
elif 25 <= temp < 35:
    print("Chaud, faites attention au soleil.")
elif 15 <= temp < 25:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")