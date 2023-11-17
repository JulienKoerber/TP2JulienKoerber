import random
def simuler_lancer_piece():
    resultat_aleatoire = random.randint(0, 100)

    if resultat_aleatoire < 50:
        resultat = "Pile !"
    else:
        resultat = "Face !"

    print(resultat)

simuler_lancer_piece()
