def AlgorytmHareNiemeyer(lista, mandaty):
    partie_mandaty = {partia: 0 for partia in lista}
    partie_wspolczynnik = {partia: glosy for partia, glosy in lista.items()}
    suma_glosow = 0
    pozostale_mandaty = mandaty

    for i in partie_wspolczynnik:
        suma_glosow += lista[i]

    for i in partie_wspolczynnik:
        partie_mandaty[i] += lista[i] * mandaty // suma_glosow
        pozostale_mandaty -= lista[i] * mandaty // suma_glosow
        partie_wspolczynnik[i] = ( lista[i] * mandaty / suma_glosow ) - partie_mandaty[i]

    if pozostale_mandaty != 0:
        for i in range (0, pozostale_mandaty):
            wsp = dict(sorted(partie_wspolczynnik.items(), key=lambda item: item[1], reverse=True))
            partie_mandaty[next(iter(wsp))] += 1
            partie_wspolczynnik[next(iter(wsp))] = 0

    return f"Mandaty: {partie_mandaty}"