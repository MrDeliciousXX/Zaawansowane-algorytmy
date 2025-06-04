def AlgorytmSainteLague(lista, mandaty):
    partie_mandaty = {partia: 0 for partia in lista}
    partie_wspolczynnik = {partia: glosy for partia, glosy in lista.items()}

    for _ in range(mandaty):
        wsp = dict(sorted(partie_wspolczynnik.items(), key=lambda item: item[1], reverse=True))
        najlepsza_partia = next(iter(wsp))

        partie_mandaty[najlepsza_partia] += 1
        partie_wspolczynnik[najlepsza_partia] = lista[najlepsza_partia] / (2 * partie_mandaty[najlepsza_partia] + 1)

    return f"Mandaty: {partie_mandaty}"