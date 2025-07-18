phrase = input("Entrez une phrase : ")
mots = phrase.split()

un_mot_sur_deux = mots[::2]
print("Un mot sur deux :", un_mot_sur_deux)