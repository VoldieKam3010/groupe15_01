panier = float(input("Valeur du panier (€) : "))

if panier >= 100:
    frais_livraison = 0
elif panier >= 50:
    frais_livraison = 5
else:
    frais_livraison = 10

total = panier + frais_livraison

print(f"Frais de livraison : {frais_livraison} €")
print(f"Total à payer : {total:.2f} €")