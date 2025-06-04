import Library
from Library import FunkcjeTestowe as Fn
INF = float('inf')

# -----Algorytmy grafowe-----

#wynik, macierz, sciezki = Library.AlgorytmJohnsona_DijkstraBellmanFord([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#   [ 2 ,INF,INF, 6 , 7 ,INF]])
#print(wynik)       # surowe dane (możesz usunąć, jeśli niepotrzebne)
#print(macierz)     # wypisana macierz odległości
#print(sciezki)     # wypisane najkrótsze ścieżki

#print(Library.AlgorytmNajblizszegoSasiada([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]], 0 ))

#print(Library.AlgorytmKruskalaWyznaczaniaDrzewaSpinajacego([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

#print(Library.AlgorytmKolorowaniaWierzcholkowSL([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

#print(Library.AlgorytmKolorowaniaWierzcholkowLF([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

#print(Library.AlgorytmKolorowaniaWierzcholkowSLF([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

#print(Library.AlgorytmKolorowaniaKrawedziNishizeki([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

#print(Library.AlgorytmWyznaczaniaDrzewaSpinajacego([
#    [INF, 4 ,INF,INF, 1 , 2 ],
#    [ 4 ,INF, 2 ,INF, 2 ,INF],
#    [INF, 2 ,INF, 8 ,INF,INF],
#    [INF,INF, 8 ,INF, 3 , 6 ],
#    [ 1 , 2 ,INF, 3 ,INF, 7 ],
#    [ 2 ,INF,INF, 6 , 7 ,INF]]))

# -----Algorytmy heurystyczne-----

#f1 = Library.AlgorytmNietoperza(Fn.paraboloid, 2, [-10,10], "minimum", 1000, 100)
#f2 = Library.AlgorytmNietoperza(Fn.paraboloid, 2, [-10,10], "maksimum", 100, 100)
#print(f"Minimum w punkcie: {f1[1]}\nWartość funkcji w punkcie: {f1[0]}\n")
#print(f"Maksimum w punkcie: {f2[1]}\nWartość funkcji w punkcie: {f2[0]}")
#f3 = Library.AlgorytmNietoperza(Fn.rastrigin, 5, [-10,10], "minimum",1000, 200)
#print(f"\n\nMinimum w punkcie: {f3[1]}\nWartość funkcji w punkcie: {f3[0]}\n")
#f4 = Library.AlgorytmNietoperza(Fn.rosenbrock, 3, [-100,100], "minimum",2000, 300)
#print(f"\n\nMinimum w punkcie: {f4[1]}\nWartość funkcji w punkcie: {f4[0]}\n")

f5 = Library.AlgorytmRoznicowy(Fn.hgbat, 2, [-100, 100], "minimum", 200, 100)
print(f"Minimum w punkcie: {f5[1]}\nWartość funkcji w punkcie: {f5[0]}\n")

# -----Algorytmy kalendarza-----
#for i in range (2010, 2031):
#    print(f"rok {i}")
#    print(Library.AlgorytmGaussaWyznaczaniaDatyWielkanocy(i))
#    print("")

#for i in range (2010, 2031):
#    print(f"rok {i}")
#    print(Library.AlgorytmMeeusaJonesaButcheraWyznaczaniaDatyWielkanocy(i))
#    print("")

#print(Library.AlgorytmWyznaczaniaLatPrzestepnych(1670))

# -----Algorytmy klasteryzacji danych-----

#Library.AlgorytmAnalizySkladowychSystemuDecyzyjnegoPCA(2)

#kmeans = Library.AlgorytmKNNDlaCentroidow(3)
#print("Centroidy:\n", kmeans["centroidy"])
#print("Pierwsze 5 wierszy z etykietami klastrów:\n", kmeans["przypisane_dane"].head())

#Library.AlgorytmKNajblizszychSasiadowKNN(3)

# -----Algorytmy modeli głosowania-----
#print(Library.AlgorytmSainteLague({"A": 1228, "B": 1012, "C": 850, "D": 543, "E": 352}, 7))
#print(Library.AlgorytmSainteLague({"A": 720, "B": 300, "C": 480}, 8))

#print(Library.AlgorytmHondt({"A": 1228, "B": 1012, "C": 850, "D": 543, "E": 352}, 7))
#print(Library.AlgorytmHondt({"A": 720, "B": 300, "C": 480}, 8))

#print(Library.AlgorytmHareNiemeyer({"A": 1228, "B": 1012, "C": 850, "D": 543, "E": 352}, 7))
#print(Library.AlgorytmHareNiemeyer({"A": 720, "B": 300, "C": 480}, 8))

# -----Algorytmy tekstu-----
#Library.WyszukanieAnagramowPoprzezZliczanie("tomek unikal komet kiedy moje list tsil test stet udes sude moje typy kalinu tets")

#Library.WyszukanieAnagramowPoprzezSortowanie("tomek unikal komet kiedy moje list tsil test stet udes sude moje typy kalinu tets")

#Library.WyszukaniePalindromow("asdlkjhlbaksbtaciicatmlwahshawalnabba")