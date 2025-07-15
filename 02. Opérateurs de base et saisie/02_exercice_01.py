#Demander deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

#Calculs
somme = a + b
difference = a-b
produit = a*b
quotient = a/b if b!=0 else "Division impossible par zéro"
division_entière = a/b if b!=0 else "Division impossible par zéro"
reste = a%b if b!=0 else ("Division impossible par zéro")

#Affichage
print(f"Somme : {somme}")
print(f"Difference : {difference}")
print(f"Produit : {produit}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entière}")
print(f"Reste : {reste}")