livres = [
    {"titre": "Python débutant", "auteur": "Alice", "année": 2009},
    {"titre": "Maîtriser python", "auteur": "Bob", "année": 2015},
    {"titre": "Python avancé", "auteur": "Charlie", "année": 2021}
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"{livre['titre']} ({livre['année']}) - {livre['auteur']}")