n = int(input("Entrez un nombre entier : "))

if n % 3 == 0 and n % 5 == 0:
    print("Ce nombre est divisible par 3 et 5.")
else:
    print("Ce nombre n'est PAS divisible par 3 et 5 à la fois.")