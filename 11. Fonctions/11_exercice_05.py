import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits
    mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

longueur = int(input("Longueur du mot de passe : "))
print("Mot de passe généré :", generer_mot_de_passe(longueur))