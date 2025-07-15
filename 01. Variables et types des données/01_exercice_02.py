#Definition des variables
nom_produit = input("Entrez le nom de votre produit :")
prix = float(input("Entrez le prix du produit:"))
stock = int(input("Entrez le stock :"))
remise = float(input("entrez le pourcentage de remise sur le produit")) #% de remise sur le produit

#Calcul du prix final
ptix_final = prix*(1-remise)

#Affichage
print(f"Produit : {nom_produit}")
print(f"prix initial : {prix} $")
print(f"remise : {remise*100}% ")
print(f"Prix_final : {ptix_final:.2f} $")
print(f"Stock disponible: {stock} ")