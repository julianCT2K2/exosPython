"""
Je veux que tu affiches un menu avec un niveau de difficulté (easy, normal, hard)
selon le choix de l'utilisateur, il aura droit à 10, 5 ou 3 essais
"""

"""
Mise en place du nombre aléatoire pour le jeu
"""
import random
n = random.randint(1,50)

"""
Jeu ou il faut trouver le bon nombre qui a été généré par hasard
"""
i = 1#variable pour l'affichage du nbre d'essai

while True:#boucle afin d'être sûr de choisir un niveau = à 1, 2 ou 3
    level = int(input("Veuillez choisir le niveau de difficulté 1, 2 ou 3\n"))  # choix du niveau de difficulté
    if level < 1 or level > 3:#Limitation du choix de diffculté à 1, 2 ou 3
        print("Il y a eu une erreur lors de la saisie du niveau")
    else:
        print("votre niveau de difficulté est,level")
        break


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