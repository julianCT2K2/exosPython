"""
Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
Si elle est multiple de 4, on regarde si elle est multiple de 100.
    Si c'est le cas, on regarde si elle est multiple de 400.
        Si c'est le cas, l'année est bissextile.
        Sinon, elle n'est pas bissextile.
    Sinon, elle est bissextile."""
an = int(input("Veux tu savoir si une année est bissextile ?\n"))
if an %400 == 0 or (an %4 == 0 and an %100 != 0):
    print(an,"est une année bissextile.")
else:
    print(an,"n'est pas une année bissextile.")