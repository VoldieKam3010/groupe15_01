phrase = input("Entrez une phrase : ")
mot_a_masquer = input("Mot à masquer : ")

masque = "*" * len(mot_a_masquer)
nouvelle_phrase = phrase.replace(mot_a_masquer, masque)

print("Phrase masquée :", nouvelle_phrase)