INF = float('inf')

def AlgorytmKruskalaWyznaczaniaDrzewaSpinajacego(graf):
    krawedzie = []

    for od, k in enumerate(graf):
        for do, wartosc in enumerate(k):
            if wartosc != INF and od < do:
                krawedzie.append([wartosc, od, do])

    S = sorted(krawedzie)
    L = []
    drzewa = []

    for krawedz in S:
        znaleziona_lista1 = next((sublista for sublista in drzewa if krawedz[1] in sublista), None)
        znaleziona_lista2 = next((sublista for sublista in drzewa if krawedz[2] in sublista), None)

        if znaleziona_lista1 != znaleziona_lista2 or znaleziona_lista1 is None:
            if znaleziona_lista1 is None and znaleziona_lista2 is None:
                drzewa.append([krawedz[1], krawedz[2]])
            elif znaleziona_lista1 is None:
                znaleziona_lista2.append(krawedz[1])
            elif znaleziona_lista2 is None and znaleziona_lista1 is not None:
                znaleziona_lista1.append(krawedz[2])
            else:
                for i in znaleziona_lista2:
                    znaleziona_lista1.append(i)
                drzewa.remove(znaleziona_lista2)
            L.append(krawedz)

        if len(L) == len(graf):
            break

    return L