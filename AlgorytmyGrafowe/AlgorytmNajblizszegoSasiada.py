INF = float('inf')

def AlgorytmNajblizszegoSasiada(graf, start):
    wierzcholki = [True] * len(graf)
    liczba_wierzcholkow = len(graf)
    sciezka = [start]
    wierzcholki[start] = False
    pozycja = start
    koszt = 0

    for i in range ( 0, liczba_wierzcholkow):
        minimum = INF
        kolejny = -1
        for index, sasiad in enumerate(graf[pozycja]):
            if sasiad != INF and sasiad < minimum and wierzcholki[index]:
                minimum = sasiad
                kolejny = index
        if kolejny != -1:
            koszt += graf[pozycja][kolejny]
            pozycja = kolejny
            wierzcholki[pozycja] = False
            sciezka.append(pozycja)
        else:
            koszt += graf[pozycja][start]
            pozycja = start
            sciezka.append(start)
    if koszt == INF:
        return "Z danego wierzchołka nie ma rozwiązania"
    else:
        return f"Droga: {sciezka}, Koszt: {koszt}"