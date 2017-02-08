"""
nombre = int(input("tape un chiffre \n"))
if nombre == 5:
    print("Gagné !!!")
elif nombre > 5:
    print("Tu es au dessus de la vérité.")
else:
    print("Tu es trop bas")
"""

"""

Jeu avec une boucle, jusqu'à la bonne réponse

while 1:
    nombre = int(input("tape un chiffre \n"))
    if nombre == 3:
        print("Tu as gagné")
        break
    elif nombre > 5:
        print("Tu es au dessus de la vérité.")
    else:
        print("Tu es trop bas")
"""

"""
Jeu avec une boucle, jusqu'à la bonne réponse et numéro réponse aléatoire
"""

import random
n = random.randint(1,50)

while True:
    nombre = int(input("tape un chiffre \n"))
    if nombre == n:
        print("Tu as gagné")
        break
    elif nombre > n:
        print("Tu es au dessus de la vérité.")
    else:
        print("Tu es trop bas")