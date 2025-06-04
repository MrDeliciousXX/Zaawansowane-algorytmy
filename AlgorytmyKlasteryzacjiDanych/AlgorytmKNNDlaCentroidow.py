import pandas as pd
import numpy as np

def StandaryzujDane(dane: pd.DataFrame):
    dane = dane.select_dtypes(include=[np.number])
    if dane.empty:
        raise ValueError("Brak liczbowych kolumn w danych wejściowych.")
    indeksy = dane.index
    dane_numpy = dane.values
    srednie = np.mean(dane_numpy, axis=0)
    dane_standaryzowane = dane_numpy - srednie
    return dane_standaryzowane, indeksy

def AlgorytmKNNDlaCentroidow(k: int, dane: pd.DataFrame = None, max_iter=300, tol=1e-4, random_state=None):
    if dane is None:
        dane = pd.read_csv("AlgorytmyKlasteryzacjiDanych/Iris.csv", header=None, names=[
            "sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
        dane = dane.sample(frac=1, random_state=random_state).reset_index(drop=True)

    # Wymuszamy konwersję kolumn na liczby
    for col in dane.select_dtypes(include='object').columns:
        dane[col], _ = pd.factorize(dane[col])

    dane_standaryzowane, indeksy = StandaryzujDane(dane)
    np.random.seed(random_state)

    # Inicjalizacja centroidów
    indeksy_centroidow = np.random.choice(len(dane_standaryzowane), k, replace=False)
    centroidy = dane_standaryzowane[indeksy_centroidow]

    for iteracja in range(max_iter):
        odleglosci = np.linalg.norm(dane_standaryzowane[:, np.newaxis] - centroidy, axis=2)
        etykiety = np.argmin(odleglosci, axis=1)

        nowe_centroidy = np.array([
            dane_standaryzowane[etykiety == i].mean(axis=0) if np.any(etykiety == i) else centroidy[i]
            for i in range(k)
        ])

        if np.allclose(centroidy, nowe_centroidy, atol=tol):
            break

        centroidy = nowe_centroidy

    wynik_df = dane.copy()
    wynik_df["klaster"] = etykiety

    return {
        "centroidy": centroidy,
        "etykiety": etykiety,
        "iteracje": iteracja + 1,
        "przypisane_dane": wynik_df
    }
