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
Jeu ou il faut trouver le bon nombre qui a été généré par hasard
"""
i = 1#variable pour l'affichage du nbre d'essai


choix = (input("Veuillez choisir le niveau de difficulté easy, medium ou hard\n"))  # choix du niveau de difficulté
if choix == "easy":
    nombreEssaiMax = 10
elif choix == "medium":
    nombreEssaiMax = 5
else:
    nombreEssaiMax = 3
print("Vous avez le droit à", nombreEssaiMax)
"""
détermine le nombre d'essai en fonction du choix user
"""

"""
Jeu trouve le chiffre
"""
while True:
    nombre = int(input("Devine le chiffre\n"))
    print("Il te reste", nombreEssaiMax - i, "coup(s)","sur",nombreEssaiMax)
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