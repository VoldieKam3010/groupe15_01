#Demande d'informations
age = int(input("Entrez votre âge : "))
pays = input("Entrez votre pays : ").strip().lower()

#Vérification de l'éligibilité
if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("✅ Vous êtes éligible au programme.")
elif age < 18:
    print("❌ Vous êtes trop jeune pour vous inscrire.")
else:
    print("❌ Désolé, ce programme est réservé aux réssortissants du Congo ou du Cameroun.")