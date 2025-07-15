anciennete = int(input("Ancienneté en années : "))
performance = int(input("Note de performance (1 à 5) : "))

if anciennete >= 5:
    if performance >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if performance >= 4:
        prime = 500
    else:
        prime = 0

print(f"Prime attribuée : {prime} €")