nombre = int(input("entrez un nombre entier : "))

if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro"

if nombre % 2 == 0:
    parite = "paire"
else:
    parite = "impaire"

print(f"Le nombre est signe} et {parite}")