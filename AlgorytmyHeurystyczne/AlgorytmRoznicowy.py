import random

def InicjalizacjaPopulacji(funkcja, wymiar, przedzial, populacja_startowa):
    populacja = []

    for _ in range(populacja_startowa):
        cechy = []
        for _ in range(wymiar):
            cechy.append(random.uniform(przedzial[0], przedzial[1]))
        wartosc = funkcja(cechy)
        osobnik = [wartosc, cechy]
        populacja.append(osobnik)

    return populacja

def Mutacja(populacja, wymiar, F, przedzial):
    mutacje = []

    for i in range(len(populacja)):
        indeksy = list(range(len(populacja)))
        indeksy.remove(i)
        i1, i2, i3 = random.sample(indeksy, 3)

        osobnik1 = populacja[i1]
        osobnik2 = populacja[i2]
        osobnik3 = populacja[i3]

        wektorMutant = []
        for j in range(wymiar):
            element = osobnik1[1][j] + F * (osobnik2[1][j] - osobnik3[1][j])
            element = max(przedzial[0], min(przedzial[1], element))
            wektorMutant.append(element)
        mutacje.append(wektorMutant)

    return mutacje

def Krzyzowanie(populacja, mutacje, CR, wymiar, funkcja):
    nowe = []

    for i in range(len(populacja)):
        cechy = []

        indeks_mutacji = random.randint(0, wymiar - 1)
        for j in range(wymiar):
            if random.random() < CR or j == indeks_mutacji:
                cechy.append(mutacje[i][j])
            else:
                cechy.append(populacja[i][1][j])
        wynik = funkcja(cechy)
        osobnik = [wynik, cechy]
        nowe.append(osobnik)

    return nowe

def Selekcja(populacja, nowe, min_max):
    nowa_populacja = []

    for i in range(len(populacja)):
        if min_max == "minimum":
            if populacja[i][0] < nowe[i][0]:
                nowa_populacja.append(populacja[i])
            else:
                nowa_populacja.append(nowe[i])
        else:
            if populacja[i][0] > nowe[i][0]:
                nowa_populacja.append(populacja[i])
            else:
                nowa_populacja.append(nowe[i])

    return nowa_populacja

def AlgorytmRoznicowy(funkcja, wymiar, przedzial, min_max, populacja_startowa, ilosc_cykli, F = 0.5, CR = 0.7):
    populacja = InicjalizacjaPopulacji(funkcja, wymiar, przedzial, populacja_startowa)

    for _ in range(ilosc_cykli):
        mutacje = Mutacja(populacja, wymiar, F, przedzial)
        nowe = Krzyzowanie(populacja, mutacje, CR, wymiar, funkcja)
        populacja = Selekcja(populacja, nowe, min_max)

    if min_max == "minimum":
        najlepszy = min(populacja, key=lambda x: x[0])
    else:
        najlepszy = max(populacja, key=lambda x: x[0])
    return najlepszy
