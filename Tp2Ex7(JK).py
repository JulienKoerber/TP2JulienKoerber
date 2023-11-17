import random

def simuler_lancer_piece():
    resultat_aleatoire = random.randint(0, 100)

probabilite_pile = 2 / 3
    if resultat_aleatoire < probabilite_pile :
        resultat = "Pile !"
    else:
        resultat = "Face !"

    print(resultat)

simuler_lancer_piece()
