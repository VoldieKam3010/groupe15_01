def calculer(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Division par 0 impossible"
        return a / b
    else:
        return "Opérateur non valide"

x = float(input("Premier nombre : "))
y = float(input("Deuxième nombre : "))
operation = input("Opération (+, -, *, /) : ")

resultat = calculer(x, y, operation)
print("Résultat :", resultat)