import random
import math

def InicjalizacjaNietoperzy(funkcja, wymiar, rozmiar_populacji, przedzial, przedzial_f):
    nietoperze = []

    for _ in range(rozmiar_populacji):
        lokalizacja = [random.uniform(przedzial[0], przedzial[1]) for _ in range(wymiar)]
        v = [0.0] * wymiar
        A = 1.0
        r = 0.0
        f = random.uniform(przedzial_f[0], przedzial_f[1])
        wartosc = funkcja(lokalizacja)
        nietoperz = [wartosc, lokalizacja, v, A, r, f]
        nietoperze.append(nietoperz)
    return nietoperze

def AktualizacjaPozycji(nietoperze, wymiar, funkcja, najlepszy, przedzial, przedzial_f, ograniczaj_predkosc=True):
    v_max = (przedzial[1] - przedzial[0]) * 0.1

    for nietoperz in nietoperze:
        nietoperz[5] = random.uniform(przedzial_f[0], przedzial_f[1])

        for d in range(wymiar):
            kierunek = najlepszy[1][d] - nietoperz[1][d]
            nietoperz[2][d] += kierunek * nietoperz[5]
            if ograniczaj_predkosc:
                nietoperz[2][d] = max(min(nietoperz[2][d], v_max), -v_max)
            nietoperz[1][d] += nietoperz[2][d]

            if nietoperz[1][d] < przedzial[0]:
                nietoperz[1][d] = przedzial[0]
                nietoperz[2][d] = 0
            elif nietoperz[1][d] > przedzial[1]:
                nietoperz[1][d] = przedzial[1]
                nietoperz[2][d] = 0
        nietoperz[0] = funkcja(nietoperz[1])
    return nietoperze

def RuchLokalnyNietoperza(nietoperze, najlepszy, min_max, funkcja, przedzial):
    for nietoperz in nietoperze:
        if random.random() > nietoperz[4]:  # r
            nowa_pozycja = [
                max(min(x + random.uniform(-1, 1) * nietoperz[3], przedzial[1]), przedzial[0])
                for x in najlepszy[1]
                #for x in nietoperz[1]
            ]
            nowa_wartosc = funkcja(nowa_pozycja)

            if random.random() < nietoperz[3]:  # A
                if min_max == "minimum":
                    if nowa_wartosc < nietoperz[0]:
                        nietoperz[1] = nowa_pozycja
                        nietoperz[0] = nowa_wartosc
                else:
                    if nowa_wartosc > nietoperz[0]:
                        nietoperz[1] = nowa_pozycja
                        nietoperz[0] = nowa_wartosc
    return nietoperze

def AlgorytmNietoperza(funkcja, wymiar, przedzial, min_max, populacja_startowa, ilosc_cykli):
    nietoperze = InicjalizacjaNietoperzy(funkcja, wymiar, populacja_startowa, przedzial, (0, 2))

    if min_max == "minimum":
        najlepszy = min(nietoperze, key=lambda n: n[0])
    else:
        najlepszy = max(nietoperze, key=lambda n: n[0])

    alpha = 0.95  # wolniejsze wygaszanie A
    gamma = 0.9   # szybszy wzrost r
    r0 = 0.1

    for cykl in range(ilosc_cykli):
        nietoperze = AktualizacjaPozycji(nietoperze, wymiar, funkcja, najlepszy, przedzial, (0, 2))
        nietoperze = RuchLokalnyNietoperza(nietoperze, najlepszy, min_max, funkcja, przedzial)

        if min_max == "minimum":
            najlepszy = min(nietoperze, key=lambda n: n[0])
        else:
            najlepszy = max(nietoperze, key=lambda n: n[0])

        for nietoperz in nietoperze:
            nietoperz[3] = max(nietoperz[3] * alpha, 0.1)  # A (amplituda dźwięku)
            nietoperz[4] = r0 + (1 - r0) * (1 - math.exp(-gamma * cykl))  # r (prawd. lokalnego ruchu)

    if min_max == "minimum":
        najlepszy = min(nietoperze, key=lambda n: n[0])
    else:
        najlepszy = max(nietoperze, key=lambda n: n[0])

    return najlepszy