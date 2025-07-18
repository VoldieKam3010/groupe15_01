# Exercice 5 - Manipulation avancée avec finally
import math

try:
    n = float(input("Entrez un nombre pour avoir sa racine carrée: "))
    racine = math.sqrt(n)
except ValueError:
    print("❌ Erreur : nombre négatif ou invalide.")
else:
    print(f"La racine carrée de {n} est : {racine:.2f}")
finally:
    print("✅ Fin du calcul.")