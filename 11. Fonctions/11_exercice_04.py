def convertisseur(usd):
    eur = usd * 0.93
    cfa = usd * 610
    gbp = usd * 0.79
    return eur, cfa, gbp

montant = float(input("Montant en dollars (USD) : "))
eur, cfa, gbp = convertisseur(montant)

print(f"{montant} USD = {eur:.2f} EUR, {cfa:.0f} FCFA, {gbp:.2f} GBP")