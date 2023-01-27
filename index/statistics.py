def countToken(titres):
    sum = 0
    for cle, valeur in titres.items():
        sum += len(valeur)
    return sum
