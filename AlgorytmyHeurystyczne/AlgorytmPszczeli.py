import random

def InicjalizacjaUla(funkcja, wymiar, przedzial, populacja_startowa):
    ul = []

    for _ in range(populacja_startowa):
        pozycja = []
        for _ in range(wymiar):
            pozycja.append(random.uniform(przedzial[0], przedzial[1]))
        wartosc = funkcja(pozycja)
        pszczola = [wartosc, pozycja]
        ul.append(pszczola)

    return ul

def SortowanieWybieranie(ul, min_max):
    ul = sorted(ul, key=lambda x: x[0], reverse=(min_max == "maksimum"))

    m = len(ul) // 4
    e = max(1, m // 5)

    miejsca = []
    elitarne = []
    for i in range(m):
        miejsca.append(ul[i])
    for i in range(e):
        elitarne.append(miejsca[i])

    return ul, miejsca, elitarne

def Przeszukiwanie(ul, elitarne, miejsca, przedzial, funkcja, min_max):
    promien = 0.1 * (przedzial[1] - przedzial[0])
    nep = max(5, len(ul) // 20)
    nsp = max(3, len(ul) // 33)
    nowy_ul = []

    for pszczola in elitarne:
        najlepsza_pszczola = pszczola

        for i in range(nep):
            nowa_pozycja = [
                min(max(x + random.uniform(-promien, promien),przedzial[0]),przedzial[1])
                for x in pszczola[1]
            ]
            nowa_wartosc = funkcja(nowa_pozycja)
            if min_max == "minimum":
                if nowa_wartosc < najlepsza_pszczola[0]:
                    najlepsza_pszczola = [nowa_wartosc, nowa_pozycja]
            else:
                if nowa_wartosc > najlepsza_pszczola[0]:
                    najlepsza_pszczola = [nowa_wartosc, nowa_pozycja]
        nowy_ul.append(najlepsza_pszczola)

    for pszczola in miejsca:
        if pszczola in elitarne:
            continue
        najlepsza_pszczola = pszczola

        for i in range(nsp):
            nowa_pozycja = [
                min(max(x + random.uniform(-promien, promien), przedzial[0]), przedzial[1])
                for x in pszczola[1]
            ]
            nowa_wartosc = funkcja(nowa_pozycja)
            if min_max == "minimum":
                if nowa_wartosc < najlepsza_pszczola[0]:
                    najlepsza_pszczola = [nowa_wartosc, nowa_pozycja]
            else:
                if nowa_wartosc > najlepsza_pszczola[0]:
                    najlepsza_pszczola = [nowa_wartosc, nowa_pozycja]
        nowy_ul.append(najlepsza_pszczola)

    return nowy_ul

def NowePszczoly(ul, populacja_startowa, funkcja, wymiar, przedzial):
    brakuje = populacja_startowa - len(ul)
    if brakuje > 0:
        ul += InicjalizacjaUla(funkcja, wymiar, przedzial, brakuje)
    return ul

def AlgorytmPszczeli(funkcja, wymiar, przedzial, min_max, populacja_startowa = 100, ilosc_cykli = 100):
    ul = InicjalizacjaUla(funkcja, wymiar, przedzial, populacja_startowa)

    for i in range(ilosc_cykli):
        ul, miejsca, elitarne = SortowanieWybieranie(ul, min_max)
        ul = Przeszukiwanie(ul, elitarne, miejsca, przedzial, funkcja, min_max)
        ul = NowePszczoly(ul, populacja_startowa, funkcja, wymiar, przedzial)

    if min_max == "minimum":
        najlepszy = min(ul, key=lambda n: n[0])
    else:
        najlepszy = max(ul, key=lambda n: n[0])

    return najlepszy