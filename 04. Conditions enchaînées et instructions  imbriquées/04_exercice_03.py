fievre = input("Avez-vous de la fièvre ? (oui/non) : ").strip().lower()

if fievre == "oui":
    douleurs = input("Avez-vous des douleurs ? (oui/non) : ").strip().lower()
    if douleurs == "oui":
        print("➡ Consulter un médecin.")
    else:
        print("➡ Reposez-vous et surveillez vos symptômes.")
else:
    toux = input("Avez-vous une toux ? (oui/non) : ").strip().lower()
    if toux == "oui":
        print("➡ Repos conseillé.")
    else:
        print("➡ Bonne santé ✅")