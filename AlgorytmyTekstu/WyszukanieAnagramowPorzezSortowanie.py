def WyszukanieAnagramowPoprzezSortowanie(tekst):
    wyrazy = tekst.split()
    for i in range(len(wyrazy)):
        for j in range(len(wyrazy)):
            if i != j:
                a = sorted(wyrazy[i])
                b = sorted(wyrazy[j])
                if a == b:
                    print(wyrazy[i])
                    print(wyrazy[j])
                    print()