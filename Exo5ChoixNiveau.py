"""
Je veux que tu affiches un menu avec un niveau de difficulté (easy, normal, hard)
selon le choix de l'utilisateur, il aura droit à 10, 5 ou 3 essais
"""

"""
Mise en place du nombre aléatoire à trouver
"""
import random
nombreADeviner = random.randint(1, 50)

"""
Fonction choix user
"""
def choix_User():
    while True:
        choix = input("Veuillez choisir le niveau de difficulté easy, medium ou hard\n")
        if choix == "easy":
            nombreEssaiMax = 10
            break
        elif choix =="medium":
            nombreEssaiMax = 5
            break
        elif choix =="hard":
            nombreEssaiMax = 3
            break
        else:
            print("Vous avez rentré un mauvais choix")

while True:
    choix = input("Veuillez choisir le niveau de difficulté easy, medium ou hard\n")  # choix du niveau de difficulté
    if choix == "easy":
        nombreEssaiMax = 10
        break
    elif choix == "medium":
        nombreEssaiMax = 5
        break
    elif choix == "hard":
        nombreEssaiMax = 3
        break
    else:
        print("Vous avez rentré une mauvaise valeur")

print("Vous avez droit à",nombreEssaiMax,"coups")
"""
Jeu trouve le chiffre
"""

i = 0#variable pour l'affichage du nbre d'essai
while True:
    nombre = int(input("Devine le chiffre\n"))
    if nombre == nombreADeviner:
        print("Tu as gagné")
        break
    elif nombre > nombreADeviner:
        print("Tu es au dessus de la vérité.")
    else:
        print("Tu es trop bas")
    i += 1
    if nombreEssaiMax == i:
        print("Tu as perdu")
        break
    print("Il te reste", nombreEssaiMax - i, "coup(s)", "sur", nombreEssaiMax)