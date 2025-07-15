#Demande d'informations à l'utilisateur
prenom = input("Entrez votre prenom :")
age = int(input("Entrez votre âge :"))
ville = input("Entrez le nom de votre ville :")
metier = input("Entrez votre metier :")

#Approximation des jours vécus
jours_vécus = age*365

#Affichage formaté
print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vécus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Metier : {metier}")