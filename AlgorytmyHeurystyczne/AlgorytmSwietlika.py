import random
import math

def odleglosc(xi, xj):
    return math.sqrt(sum((xi_k - xj_k) ** 2 for xi_k, xj_k in zip(xi, xj)))

def atrakcyjnosc(beta0, gamma, r):
    return beta0 * math.exp(-gamma * (r ** 2))

def RozplenienieSwietlikow(funkcja, wymiar, przedzial, populacja_startowa):
    swietliki = []

    for _ in range(populacja_startowa):
        lokalizacja = []
        for _ in range(wymiar):
            lokalizacja.append(random.uniform(przedzial[0], przedzial[1]))
        wynik = funkcja(lokalizacja)
        swietlik = [wynik, lokalizacja]
        swietliki.append(swietlik)

    return swietliki

def Ruch(swietliki, funkcja, min_max, przedzial, beta0=1.0, gamma=1.0, alpha=0.2):
    nowa_lista = []

    for i in range(len(swietliki)):
        xi = swietliki[i][1]
        fi = swietliki[i][0]
        nowa_pozycja = xi[:]

        for j in range(len(swietliki)):
            if i == j:
                continue

            xj = swietliki[j][1]
            fj = swietliki[j][0]

            if (min_max == "minimum" and fj < fi) or (min_max == "maksimum" and fj > fi):
                r = odleglosc(xi, xj)
                beta = atrakcyjnosc(beta0, gamma, r)

                nowa_pozycja = [
                    min(max(xi_k + beta * (xj_k - xi_k) + alpha * (random.random() - 0.5), przedzial[0]), przedzial[1])
                    for xi_k, xj_k in zip(nowa_pozycja, xj)
                ]

        nowa_wartosc = funkcja(nowa_pozycja)
        nowa_lista.append([nowa_wartosc, nowa_pozycja])

    return nowa_lista

def AlgorytmSwietlika(funkcja, wymiar, przedzial, min_max, populacja_startowa, ilosc_cykli):
    swietliki = RozplenienieSwietlikow(funkcja, wymiar, przedzial, populacja_startowa)

    for i in range(ilosc_cykli):
        swietliki = Ruch(swietliki, funkcja, min_max, przedzial)

    if min_max == "minimum":
        najlepszy = min(swietliki, key=lambda n: n[0])
    else:
        najlepszy = max(swietliki, key=lambda n: n[0])

    return najlepszy