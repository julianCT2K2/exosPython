# tu tapes ta réponse si le nombre est trop grand,l'ordi te dit trop grand et tu peu retenter ta chance
# sinon, si c'est trop petit, il te dit trop petit et tu rééessayes
"""nombre = int(input("tape un chiffre \n"))
if nombre == 5:
    print("Gagné !!!")
elif nombre > 5:
    print("Tu es au dessus de la vérité.")
else:
    print("Tu es trop bas")"""

#nombre = int(input("tape un chiffre \n"))

while 1:
    nombre = int(input("tape un chiffre \n"))
    if nombre == 5:
        print("Tu as gagné")
        break
    elif nombre > 5:
        print("Tu es au dessus de la vérité.")
    else:
        print("Tu es trop bas")