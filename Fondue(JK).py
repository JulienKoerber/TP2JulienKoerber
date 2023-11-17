BASE = 4
fromage_base = 800.0
eau_base = 2
ail_base = 2
pain_base = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

fromage = fromage_base * nbConvives / BASE
eau = eau_base * nbConvives / BASE
ail = ail_base * nbConvives / BASE
pain = pain_base * nbConvives / BASE

print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personne(s), il vous faut :")
print(f"- {fromage:.1f} gr de fromage")
print(f"- {eau:.1f} dl d'eau")
print(f"- {ail:.1f} gousse(s) d'ail")
print(f"- {pain:.1f} gr de pain")
