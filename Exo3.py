
i = 1900
while i < 2017:
    an = i += 1
    if an %4 == 0 and an %100 == 0:
        if an %400 == 0:
            print(an,"est une année bissextile.")
    else:
        print(an,"n'est pas une année bissextile.")