role = input("Votre rôle (employé, visiteur, sécurité) : ").strip().lower()

if role == "employé":
    badge = input("Badge valide ? (oui/non) : ").strip().lower()
    if badge == "oui":
        print("✅ Accès autorisé.")
    else:
        print("❌ Accès refusé, badge invalide.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous ? (oui/non) : ").strip().lower()
    if rdv == "oui":
        print("✅ Accès autorisé.")
    else:
        print("❌ Accès refusé, pas de rendez-vous.")
elif role == "sécurité":
    print("✅ Accès direct autorisé.")
else:
    print("❌ Accès refusé, rôle inconnu.")