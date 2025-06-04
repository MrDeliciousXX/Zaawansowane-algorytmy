import random
import numpy as np
from scipy.special import gamma

def InicjalizacjaGniazd(ilosc, przedzial, wymiar):
    gniazda = []
    for _ in range(ilosc):
        gniazdo = []
        for __ in range(wymiar):
            gniazdo.append(random.uniform(przedzial[0], przedzial[1]))
        gniazda.append([None, gniazdo])

    return gniazda

def OcenaGniazd(funkcja, gniazda):
    for i in range(len(gniazda)):
        gniazda[i][0] = funkcja(gniazda[i][1])

    return gniazda

def LotLevyego(gniazda, funkcja, min_max, przedzial, a=0.01, lam=1.5):
    sigma_u = (gamma(1 + lam) * np.sin(np.pi * lam / 2) / (gamma((1 + lam) / 2) * lam * 2 ** ((lam - 1) / 2))) ** (1 / lam)

    for i, gniazdo in enumerate(gniazda):
        nowe_cechy = []

        for cecha in gniazdo[1]:
            u = np.random.normal(0, sigma_u)
            v = np.random.normal(0, 1)
            lot = u / abs(v) ** (1 / lam)
            if cecha + a * lot > przedzial[1]:
                nowe_cechy.append(przedzial[1])
            elif cecha + a * lot < przedzial[0]:
                nowe_cechy.append(przedzial[0])
            else:
                nowe_cechy.append(cecha + a * lot)

        nowa_wartosc = funkcja(nowe_cechy)

        if (min_max == "maksimum" and nowa_wartosc > gniazdo[0]) or \
                (min_max == "minimum" and nowa_wartosc < gniazdo[0]):
            gniazda[i] = [nowa_wartosc, nowe_cechy]

    return gniazda

def PodmianaGniazd(gniazda, min_max, ile_wymieniamy, p_wymiany, funkcja, wymiar, przedzial):
    posortowane = sorted(gniazda, key=lambda x: x[0], reverse=True)
    nowe_gniazda = []
    for i in range(len(gniazda)):
        if min_max == "maksimum":
            if i < len(gniazda) - (len(gniazda)*ile_wymieniamy):
                nowe_gniazda.append(posortowane[i])
            elif random.random() < p_wymiany:
                nowe = [None,[]]
                for _ in range(wymiar):
                    nowe[1].append(random.uniform(przedzial[0], przedzial[1]))
                nowe[0] = funkcja(nowe[1])
                nowe_gniazda.append(nowe)
            else:
                nowe_gniazda.append(posortowane[i])
        else:
            if i > len(gniazda)*ile_wymieniamy:
                nowe_gniazda.append(posortowane[i])
            elif random.random() < p_wymiany:
                nowe = [None,[]]
                for _ in range(wymiar):
                    nowe[1].append(random.uniform(przedzial[0], przedzial[1]))
                nowe[0] = funkcja(nowe[1])
                nowe_gniazda.append(nowe)
            else:
                nowe_gniazda.append(posortowane[i])

    return nowe_gniazda

def Cykl(funkcja, gniazda, min_max, wymiar, przedzial):
    gniazdaOcenione = OcenaGniazd(funkcja, gniazda)
    gniazdaLot = LotLevyego(gniazdaOcenione, funkcja, min_max, przedzial)
    gniazdaPodmienione = PodmianaGniazd(gniazdaLot, min_max, 0.5, 0.4, funkcja, wymiar, przedzial)

    return gniazdaPodmienione

def AlgorytmKukulki(funkcja, wymiar, przedzial, min_max, populacja_startowa = 1000, ilosc_cykli = 100):
    gniazda = InicjalizacjaGniazd(populacja_startowa, przedzial, wymiar)
    for i in range(ilosc_cykli):
        gniazda = Cykl(funkcja, gniazda, min_max, wymiar, przedzial)

    if min_max == "minimum":
        return min(gniazda, key=lambda x: x[0])
    else:
        return max(gniazda, key=lambda x: x[0])