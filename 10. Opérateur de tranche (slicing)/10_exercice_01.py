mot = input("Entrez un mot d'au moins 5 lettres : ")

if len(mot) >= 5:
    milieu = mot[2:-2]
    print("Milieu :", milieu)
else:
    print("Mot trop court !")