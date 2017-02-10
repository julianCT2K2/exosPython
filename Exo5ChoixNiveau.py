import random
n = random.randint(1,50)
i = 0
while True:
    nombre = int(input("tape un chiffre \n"))
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