import pandas as pd
import numpy as np
from collections import Counter

def Euklides(x1: tuple, x2: tuple) -> float:
    if len(x1) != len(x2):
        raise ValueError("Tuple mają różną długość.")
    return np.sqrt(np.sum([(x1[i] - x2[i]) ** 2 for i in range(len(x1))]))

def KlasyfikacjaKNN(X_tr: pd.DataFrame, y_tr: pd.Series, X_te: pd.DataFrame, k=3, metryka=Euklides):
    etykiety_predykcji = []

    for wiersz_testowy in X_te.itertuples(index=False):
        odleglosci = []

        for wiersz_treningowy in X_tr.itertuples(index=False):
            dist = metryka(tuple(wiersz_testowy), tuple(wiersz_treningowy))
            odleglosci.append(dist)

        indeksy_posortowane = np.argsort(odleglosci)[:k]
        najblizsze_etykiety = y_tr.iloc[indeksy_posortowane]
        najczestsza_etykieta = Counter(najblizsze_etykiety).most_common(1)[0][0]
        etykiety_predykcji.append(najczestsza_etykieta)

    return etykiety_predykcji

def AlgorytmKNajblizszychSasiadowKNN(k=3):
    dane = pd.read_csv("AlgorytmyKlasteryzacjiDanych/Iris.csv")
    dane = dane.rename(columns={
        "SepalLengthCm": "sepal_length",
        "SepalWidthCm": "sepal_width",
        "PetalLengthCm": "petal_length",
        "PetalWidthCm": "petal_width",
        "Species": "species"
    })

    dane = dane.sample(frac=1).reset_index(drop=True)

    X = dane[["sepal_length", "sepal_width", "petal_length", "petal_width"]].apply(pd.to_numeric, errors='coerce')
    y = dane["species"]

    if X.isnull().any().any():
        raise ValueError("Dane wejściowe zawierają puste wartości po konwersji na liczby.")

    podzial = int(len(dane) * 0.7)
    X_tren = X.iloc[:podzial]
    X_test = X.iloc[podzial:]
    y_tren = y.iloc[:podzial]
    y_test = y.iloc[podzial:]

    predykcje = KlasyfikacjaKNN(X_tren, y_tren, X_test, k=k)

    trafienia = sum(pred == prawda for pred, prawda in zip(predykcje, y_test))
    dokladnosc = trafienia / len(y_test)

    print("Predykcje:", predykcje)
    print("Rzeczywiste:", y_test.tolist())
    print(f"Dokładność: {dokladnosc:.2%}")

    return predykcje
