def addition(nb):
    i = 0
    while i < 100:
        print(nb,"*",i + 1,"=",nb * (i + 1))
        i += 1

print(addition(int(input("Entrez un chiffre\n"))))
