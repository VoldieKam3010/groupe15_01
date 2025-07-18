email = input("Entrez votre adresse email : ").strip()

if email.endswith("@gmail.com"):
    print("✅ Adresse email valide (Gmail)")
else:
    print("❌ Cette adresse n'est pas valide")