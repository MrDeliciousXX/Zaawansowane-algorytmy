INF = float('inf')

def AlgorytmJohnsona_DijkstraBellmanFord(graf):

    bellman = AlgorytmBellmanFord(graf, 0)

    if bellman is None:
        return None
    else:
        graf2 = [[INF] * len(graf) for _ in range(len(graf))]

        for i in range(len(graf2)):
            for j in range(len(graf2)):
                graf2[i][j] = graf[i][j] + bellman[i][0] - bellman[j][0]

        wynik = []
        for n in range(len(graf)):
            dijkstra = AlgorytmDijkstra(graf2, n)

            for j in range(len(graf)):
                if dijkstra[j][0] != INF:
                    dijkstra[j][0] = dijkstra[j][0] - bellman[n][0] + bellman[j][0]

            wynik.append(dijkstra)

        # Przygotuj tekst do wypisania macierzy odległości
        tekst_macierz = "Macierz najkrótszych odległości:\n"
        n = len(wynik)
        tekst_macierz += "     " + "  ".join(f"{i:5}" for i in range(n)) + "\n"
        tekst_macierz += "    " + "------" * n + "\n"
        for i, row in enumerate(wynik):
            formatted_row = "  ".join(f"{el[0]:5}" if el[0] != INF else "  INF" for el in row)
            tekst_macierz += f"{i} | {formatted_row}\n"

        # Przygotuj tekst do wypisania ścieżek
        tekst_sciezki = "Najkrótsze ścieżki:\n"
        for start in range(len(wynik)):
            for koniec in range(len(wynik)):
                if wynik[start][koniec][0] != INF and start != koniec:
                    sciezka = [koniec]
                    poprzednik = wynik[start][koniec][1]

                    while poprzednik != -1:
                        sciezka.append(poprzednik)
                        poprzednik = wynik[start][poprzednik][1]

                    sciezka.reverse()
                    tekst_sciezki += f"{start} → {koniec}: {wynik[start][koniec][0]}, ścieżka: {' → '.join(map(str, sciezka))}\n"

        # Zwróć wszystko jako krotkę
        return wynik, tekst_macierz, tekst_sciezki

def AlgorytmBellmanFord(graf, start):
    wartosci = [[INF, -1] for _ in range(len(graf))] #dla kazdego wierzcholka, wartosci koszt dotarcia oraz poprzedni wierzcholek
    wartosci[start][0] = 0

    for _ in range (0, len(graf) - 1):
        stan = [wiersz[:] for wiersz in wartosci]
        for od, krawedzie in enumerate(graf):
            for do, wartosc in enumerate(krawedzie):
                if wartosci[do][0] > wartosci[od][0] + wartosc and wartosc != INF:
                    wartosci[do][0] = wartosci[od][0] + wartosc
                    wartosci[do][1] = od
        if stan == wartosci:
            break

    for od in range(len(graf)):
        for do in range(len(graf)):
            wartosc = graf[od][do]
            if wartosc != INF and wartosci[do][0] > wartosci[od][0] + wartosc:
                print('Graf zawiera cykl ujemny!')
                return None
    return wartosci

def AlgorytmDijkstra(graf, start):
    wartosci = [[INF, -1] for _ in range(len(graf))]
    wartosci[start][0] = 0
    wierzcholki = list(range(len(graf)))

    while len(wierzcholki) > 0:
        v = min(wierzcholki, key=lambda i: wartosci[i][0])
        wierzcholki.remove(v)
        for u, k in enumerate(graf[v]):
            if wartosci[v][0] + k < wartosci[u][0] and k != INF:
                wartosci[u][0] = k + wartosci[v][0]
                wartosci[u][1] = v

    return wartosci