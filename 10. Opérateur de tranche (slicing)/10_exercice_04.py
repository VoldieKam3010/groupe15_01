numero = input("Entrez un numéro de téléphone (ex : 0897654321) : ")

masque = "*" * (len(numero) - 3) + numero[-3:]
print("Numéro masqué :", masque)