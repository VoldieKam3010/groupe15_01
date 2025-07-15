plat = input("Type de plat (viande, poisson, végétarien) : ").strip().lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant, à point, bien cuit) : ")
    print(f"Vous avez choisi une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron, beurre) : ")
    print(f"Vous avez choisi un poisson sauce {sauce}.")
elif plat == "végétarien":
    choix = input("Voulez-vous une salade ou des pâtes ? ")
    print(f"Vous avez choisi un plat végétarien : {choix}.")
else:
    print("Option inconnue.")