an = int(input("Veux tu savoir si une année est bissextile ?\n"))
if an %4 == 0 and an %100 == 0:
    if an %400 == 0:
        print(an,"est une année bissextile.")
else:
    print(an,"n'est pas une année bissextile.")