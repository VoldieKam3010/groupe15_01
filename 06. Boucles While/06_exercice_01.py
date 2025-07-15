import random

#Génération d'un nombre aléatoire
secret = random.randint(1,100)
trouve = False

print("J'ai choisi un nombre entre 1 et 100. Devine-le !")

while not trouve:
    essai = int(input("Votre proposition : "))
    if essai < secret:
        print("Trop petit !")
    elif essai > secret:
        print("Trop grand !")
    else:
        print("Bravo ! Vous avez trouvé 🎉")