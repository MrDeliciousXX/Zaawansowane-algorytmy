import random
import numpy as np

def InicjalizacjaRoju(ilosc, przedzial, wymiar, funkcja):
    czastki = []
    predkosci = []
    p_best = []
    p_best_wartosci = []

    for _ in range(ilosc):
        czastka = [random.uniform(przedzial[0], przedzial[1]) for _ in range(wymiar)]
        predkosc = [random.uniform(-abs(przedzial[1] - przedzial[0]), abs(przedzial[1] - przedzial[0])) for _ in
                    range(wymiar)]

        wartosc = funkcja(czastka)

        czastki.append([wartosc, czastka])
        predkosci.append(predkosc)
        p_best.append(czastka[:])
        p_best_wartosci.append(wartosc)

    return czastki, predkosci, p_best, p_best_wartosci

def RuchCzastek(rojCzastek, predkosci, przedzial, funkcja):
    nowe = []

    for i in range(len(rojCzastek)):
        nowa_pozycja = [
            max(przedzial[0], min(przedzial[1], rojCzastek[i][1][j] + predkosci[i][j]))
            for j in range(len(rojCzastek[i][1]))
        ]

        nowa_wartosc = funkcja(nowa_pozycja)
        nowe.append([nowa_wartosc, nowa_pozycja])

    return nowe

def AktualizujPBest(rojCzastek, p_best, p_best_wartosci, min_max):
    for i in range(len(rojCzastek)):
        nowa_wartosc, nowa_pozycja = rojCzastek[i]

        if (min_max == "maksimum" and nowa_wartosc > p_best_wartosci[i]) or (min_max == "minimum" and nowa_wartosc < p_best_wartosci[i]):
            p_best[i] = nowa_pozycja[:]
            p_best_wartosci[i] = nowa_wartosc

def ZmianaPredkosci(predkosci, rojCzastek, p_best, g_best, fi_p, fi_s):
    nowePredkosci = []

    for i in range(len(predkosci)):
        nowa_predkosc = [
            predkosci[i][j] +
            fi_p * random.uniform(0, 1) * (p_best[i][j] - rojCzastek[i][1][j]) +
            fi_s * random.uniform(0, 1) * (g_best[1][j] - rojCzastek[i][1][j])
            for j in range(len(rojCzastek[i][1]))
        ]
        nowePredkosci.append(nowa_predkosc)

    return nowePredkosci

def Cykl(rojCzastek, predkosci, p_best, p_best_wartosci, funkcja, przedzial, min_max, fi_p, fi_s):
    g_best = min(zip(p_best_wartosci, p_best), key=lambda x: x[0]) if min_max == "minimum" else max(zip(p_best_wartosci, p_best), key=lambda x: x[0])

    predkosci = ZmianaPredkosci(predkosci, rojCzastek, p_best, g_best, fi_p, fi_s)
    rojCzastek = RuchCzastek(rojCzastek, predkosci, przedzial, funkcja)

    AktualizujPBest(rojCzastek, p_best, p_best_wartosci, min_max)

    return rojCzastek, predkosci, p_best, p_best_wartosci

def AlgorytmRojuCzastek(funkcja, wymiar, przedzial, min_max = "minimum", populacja_startowa = 1000, ilosc_cykli = 100, fi_p = 1, fi_s = 1):
    rojCzastek, predkosci, p_best, p_best_wartosci = InicjalizacjaRoju(populacja_startowa, przedzial, wymiar, funkcja)

    for _ in range(ilosc_cykli):
        rojCzastek, predkosci, p_best, p_best_wartosci = Cykl(rojCzastek, predkosci, p_best, p_best_wartosci, funkcja, przedzial, min_max, fi_p, fi_s)

    najlepsze_rozwiazanie = min(zip(p_best_wartosci, p_best), key=lambda x: x[0]) if min_max == "minimum" else max(zip(p_best_wartosci, p_best), key=lambda x: x[0])

    return najlepsze_rozwiazanier