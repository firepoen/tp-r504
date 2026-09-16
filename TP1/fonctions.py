def puissance(a, b):
    if not type(a) is int:
        raise TypeError("Seuls les nombres entiers sont autorisés")

    if not type(b) is int:
        raise TypeError("Seuls les nombres entiers sont autorisés")

    if a == 0 and b < 0:
        raise Exception("Opération indéfinie")

    resultat = 1

    if b >= 0:
        for i in range(b):
            resultat = resultat * a
    else:
        for i in range(-b):
            resultat = resultat * a
        resultat = 1 / resultat

    return resultat
