import random
import numpy as np

def InicjalizacjaPopulacji(wymiar, rozmiar_populacji, przedzial):
    populacja = []
    for _ in range(rozmiar_populacji):
        chromosom = []
        osobnik = [None]
        for __ in range(wymiar):
            chromosom.append(random.uniform(przedzial[0], przedzial[1]))
        osobnik.append(chromosom)
        populacja.append(osobnik)


    return populacja

def OcenaPopulacji(funkcja, populacja):
    for i in range(len(populacja)):
        populacja[i][0] = funkcja(populacja[i][1])

    return populacja

def Selekcja(populacja, metoda, cel, rozmiar_grupy = 2):
    wyselekcjonowane_osobniki = []

    if metoda == "turniejowa":

        indeksy = list(range(len(populacja)))
        random.shuffle(indeksy)
        turniej = []

        for i in range(0, len(populacja) - (len(populacja) % rozmiar_grupy), rozmiar_grupy):
            grupa = []
            for j in range(rozmiar_grupy):
                grupa.append(populacja[indeksy[i + j]])
            turniej.append(grupa)

        pozostali = []
        for i in range(len(populacja) - (len(populacja) % rozmiar_grupy),
                        len(populacja)):
            pozostali.append(populacja[indeksy[i]])

        for osobnik in pozostali:
            random.choice(turniej).append(osobnik)

        for rywalizacja in turniej:
            if cel == "maksimum":
                wyselekcjonowane_osobniki.append(max(rywalizacja, key=lambda x: x[0]))
            else:
                wyselekcjonowane_osobniki.append(min(rywalizacja, key=lambda x: x[0]))
    #elif metoda == "ruletkowa":

    #elif metoda == "rankingowa":

    #elif metoda == "elitarna":

    return wyselekcjonowane_osobniki

def Krzyzowanie(populacja, cel, prawdopodobienstwo):
    potomstwo = []

    indeksy = list(range(len(populacja)))

    if len(populacja) % 2 != 0:
        if cel == "maksimum":
            indeksy.remove(populacja.index(min(populacja, key=lambda x: x[0])))
        else:
            indeksy.remove(populacja.index(max(populacja, key=lambda x: x[0])))
    random.shuffle(indeksy)

    for i in range(0, len(indeksy), 2):
        if random.random() <= prawdopodobienstwo:
            rodzic1 = populacja[indeksy[i]][1]
            rodzic2 = populacja[indeksy[i+1]][1]
            punkt_podzialu = random.randint(1, len(rodzic1)-1)
            dziecko1 = rodzic1[:punkt_podzialu] + rodzic2[punkt_podzialu:]
            dziecko2 = rodzic2[:punkt_podzialu] + rodzic1[punkt_podzialu:]
            potomstwo.append([None, dziecko1])
            potomstwo.append([None, dziecko2])

    return potomstwo

def Mutacja(populacja, przedzial, prawdopodobienstwo):

    for index1, osobnik in enumerate(populacja):
        for index2, gen in enumerate(osobnik[1]):
            if random.random() <= prawdopodobienstwo:
                osobnik[1][index2] = random.uniform(0.95 * gen, 1.05 * gen)
                if osobnik[1][index2] < przedzial[0]:
                    osobnik[1][index2] = przedzial[0]
                elif osobnik[1][index2] > przedzial[1]:
                    osobnik[1][index2] = przedzial[1]
        populacja[index1] = osobnik

    return populacja

def Cykl(funkcja, wymiar, populacja, cel, metoda, przedzial, p_mutacja, p_potomek):
    ocena = OcenaPopulacji(funkcja, populacja)
    selekcja = Selekcja(ocena, metoda, cel)
    if wymiar > 1:
        potomstwo = Krzyzowanie(selekcja, cel, p_potomek)
    else:
        potomstwo = selekcja
    if len(potomstwo) == 0:
        potomstwo = selekcja
    zmutowane = Mutacja(potomstwo, przedzial, p_mutacja)

    return zmutowane

def AlgorytmGenetyczny(funkcja, wymiar, przedzial, min_max, populacja_startowa = 1000, ilosc_pokolen = 100, metoda = "turniejowa"):
    p_mutacja = 0.1
    p_potomek = 0.8

    populacja = InicjalizacjaPopulacji(wymiar, populacja_startowa, przedzial)
    for i in range(ilosc_pokolen):
        populacja = Cykl(funkcja, wymiar, populacja, min_max, metoda, przedzial, p_mutacja, p_potomek)
        if len(populacja) == 1:
            break

    ostatnie_pokolenie = OcenaPopulacji(funkcja, populacja)
    if min_max == "maksimum":
        najlepszy_osobnik = max(ostatnie_pokolenie, key=lambda x: x[0])
    else:
        najlepszy_osobnik = min(ostatnie_pokolenie, key=lambda x: x[0])
    return najlepszy_osobnik