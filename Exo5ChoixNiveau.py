"""
Je veux que tu affiches un menu avec un niveau de difficulté (easy, normal, hard)
selon le choix de l'utilisateur, il aura droit à 10, 5 ou 3 essais
"""

"""
Mise en place du nombre aléatoire à trouver
"""
import random
n = random.randint(1,50)

"""
Jeu ou il faut trouver le bon nombre qui a été généré par hasard
"""
i = 1#variable pour l'affichage du nbre d'essai


level = (input("Veuillez choisir le niveau de difficulté easy, medium ou hard\n"))  # choix du niveau de difficulté
if level == "easy":
   level = 10
elif level == "medium":
   level = 5
else:
   level = 3


"""
détermine le nombre d'essai en fonction du choix user
"""
while True:
    nombre = int(input("Devine le chiffre\n"))
    if nombre == n or nombre != n:
        print("Essai",i)
    if nombre == n:
        print("Tu as gagné")
        break
    elif nombre > n:
        print("Tu es au dessus de la vérité.")
    else:
        print("Tu es trop bas")
    i += 1