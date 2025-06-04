def WyszukanieAnagramowPoprzezZliczanie(tekst):
    zliczanie_liter = {}
    wyrazy = tekst.split()

    for wyraz in wyrazy:
        liczba_liter = {}
        for litera in wyraz:
            liczba_liter[litera] = liczba_liter.get(litera, 0) + 1
        zliczanie_liter[wyraz] = liczba_liter

    for i in range(len(wyrazy)):
        for j in range(i + 1, len(wyrazy)):
            if zliczanie_liter[wyrazy[i]] == zliczanie_liter[wyrazy[j]]:
                print(f"Anagramy: {wyrazy[i]} i {wyrazy[j]}")
                print()