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

def ObliczMacierzKowariancji(dane: np.ndarray):
    return np.cov(dane, rowvar=False)

def ObliczWartosciIWektoryWlasne(macierz_kow: np.ndarray):
    wartosci, wektory = np.linalg.eigh(macierz_kow)
    return wartosci, wektory

def SortujWektoryWlasne(wartosci: np.ndarray, wektory: np.ndarray, k: int):
    indeksy = np.argsort(wartosci)[::-1]
    wartosci_posortowane = wartosci[indeksy]
    wektory_top_k = wektory[:, indeksy[:k]]
    return wartosci_posortowane, wektory_top_k

def ObliczPCA(dane: np.ndarray, wektory_top_k: np.ndarray):
    return np.dot(dane, wektory_top_k)

def WypiszWariancje(wartosci: np.ndarray, k: int):
    suma = np.sum(wartosci)
    wyjasniona = (wartosci[:k] / suma).tolist()
    print("Procent wyjaśnionej wariancji:", wyjasniona)

def AlgorytmAnalizySkladowychSystemuDecyzyjnegoPCA(k: int, dane: pd.DataFrame = None):
    if dane is None:
        # Wczytaj z nagłówkiem, odfiltruj 'Id'
        dane = pd.read_csv("AlgorytmyKlasteryzacjiDanych/Iris.csv")
        dane = dane.drop(columns=["Id"])  # usuń kolumnę Id

        # Zmień nazwy kolumn na Twoje standardowe, jeśli chcesz:
        dane.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

        dane = dane.sample(frac=1).reset_index(drop=True)

        # Wymuś konwersję kolumn na float
        for col in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
            dane[col] = pd.to_numeric(dane[col], errors='coerce')

        # Sprawdź, czy są braki
        if dane[["sepal_length", "sepal_width", "petal_length", "petal_width"]].isnull().any().any():
            raise ValueError("Są puste wartości w danych numerycznych po konwersji.")

    # dalej PCA tak jak było...
    dane_standaryzowane, indeksy = StandaryzujDane(dane)
    macierz_kow = ObliczMacierzKowariancji(dane_standaryzowane)
    wartosci, wektory = ObliczWartosciIWektoryWlasne(macierz_kow)
    wartosci, wektory_top_k = SortujWektoryWlasne(wartosci, wektory, k)
    dane_pca = ObliczPCA(dane_standaryzowane, wektory_top_k)
    WypiszWariancje(wartosci, k)
    kolumny_pca = [f"PC{i + 1}" for i in range(k)]
    return pd.DataFrame(dane_pca, columns=kolumny_pca, index=indeksy)