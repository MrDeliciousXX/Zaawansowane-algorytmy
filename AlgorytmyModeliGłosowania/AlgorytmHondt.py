def AlgorytmHondt(lista, mandaty):
    partie_mandaty = {partia: 0 for partia in lista}
    partie_wspolczynnik = {partia: glosy for partia, glosy in lista.items()}

    for i in range (0, mandaty):
        wsp = dict(sorted(partie_wspolczynnik.items(), key=lambda item: item[1], reverse=True))
        top = next(iter(wsp))
        partie_mandaty[top] += 1
        partie_wspolczynnik[top] = lista[top] / (1 + partie_mandaty[top])

    return f"Mandaty: {partie_mandaty}"