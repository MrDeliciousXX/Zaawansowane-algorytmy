import random
import math
import numpy as np

def InicjalizacjaMrowiska(funkcja, wymiar, przedzial, populacja_mrowek):
    mrowki = []
    for _ in range(populacja_mrowek):
        mrowka = [None,[]]
        for _ in range(wymiar):
            mrowka[1].append(random.uniform(przedzial[0], przedzial[1]))
        mrowka[0] = funkcja(mrowka[1])
        mrowki.append(mrowka)

    feromony = [1.0] * len(mrowki)
    return mrowki, feromony

def Kartezjusz(p1, p2, wymiar):
    suma_kwadratow = sum((p1[k] - p2[k]) ** 2 for k in range(wymiar))
    dlugosc_sciezki = math.sqrt(suma_kwadratow)
    return dlugosc_sciezki

def Odleglosc(mrowka, mrowki, wymiar):
    odleglosc = 0.0

    for punkt in mrowki:
        dlugosc_sciezki = Kartezjusz(mrowka, punkt, wymiar)
        if dlugosc_sciezki != 0:
            odleglosc += 1 / dlugosc_sciezki

    return odleglosc

def AktualizacjaFeromonow(feromony, mrowki, wymiar, wyparowanie):
    for i in range(len(mrowki)):
        pozycja_i = mrowki[i][1]
        inne_pozycje = [m[1] for m in mrowki]
        gamma = Odleglosc(pozycja_i, inne_pozycje, wymiar)
        feromony[i] = (1 - wyparowanie) * feromony[i] + gamma
    return feromony

def WybierzNowaPozycje(i, mrowki, feromony, wymiar, alpha=2, sigma=0.1):
    pozycja_i = mrowki[i][1]
    prawdopodobienstwa = []

    for j in range(len(mrowki)):
        if j == i:
            prawdopodobienstwa.append(0.0)
            continue
        odleglosc = Kartezjusz(pozycja_i, mrowki[j][1], wymiar)
        if odleglosc == 0:
            odleglosc = 1e-6  # uniknij dzielenia przez zero
        waga = (feromony[j] ** alpha) / odleglosc
        prawdopodobienstwa.append(waga)

    # Normalizacja
    suma = sum(prawdopodobienstwa)
    if suma == 0:
        # wszystkie wagi 0 – wybieramy losowo
        indeks_wzorca = random.choice([j for j in range(len(mrowki)) if j != i])
    else:
        prawdopodobienstwa = [p / suma for p in prawdopodobienstwa]
        indeks_wzorca = np.random.choice(len(mrowki), p=prawdopodobienstwa)

    # Tworzymy nową pozycję na podstawie wybranej mrówki + mutacja
    nowa_pozycja = []
    for k in range(wymiar):
        wsp = mrowki[indeks_wzorca][1][k]
        mutacja = random.gauss(0, sigma)
        nowa_pozycja.append(wsp + mutacja)

    return nowa_pozycja

def AlgorytmMrowkowy(funkcja, wymiar, przedzial, min_max, populacja_mrowek = 200, wspolczynnik_wyparowania = 0.35 ,ilosc_cykli = 100):
    mrowki, feromony = InicjalizacjaMrowiska(funkcja, wymiar, przedzial, populacja_mrowek)
    feromony = AktualizacjaFeromonow(feromony, mrowki, wymiar, wspolczynnik_wyparowania)

    najlepsza_mrowka = min(mrowki, key=lambda m: m[0]) if min_max == "minimum" else max(mrowki, key=lambda m: m[0])

    for cykl in range(ilosc_cykli):
        nowe_mrowki = []
        for i in range(populacja_mrowek):
            nowa_pozycja = WybierzNowaPozycje(i, mrowki, feromony, wymiar)
            nowa_pozycja = [min(max(x, przedzial[0]), przedzial[1]) for x in nowa_pozycja]
            nowa_wartosc = funkcja(nowa_pozycja)
            nowe_mrowki.append([nowa_wartosc, nowa_pozycja])

        mrowki = nowe_mrowki
        feromony = AktualizacjaFeromonow(feromony, mrowki, wymiar, wspolczynnik_wyparowania)

        aktualna_najlepsza = min(mrowki, key=lambda m: m[0]) if min_max == "minimum" else max(mrowki, key=lambda m: m[0])
        if (min_max == "minimum" and aktualna_najlepsza[0] < najlepsza_mrowka[0]) or \
                (min_max == "maksimum" and aktualna_najlepsza[0] > najlepsza_mrowka[0]):
            najlepsza_mrowka = aktualna_najlepsza

    return najlepsza_mrowka