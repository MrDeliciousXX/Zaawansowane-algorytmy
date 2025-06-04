def AlgorytmKolorowaniaWierzcholkowLF(matrix: list[list[int]]) -> dict:
    INF = float('inf')

    n = len(matrix)
    # Sprawdzenie, czy macierz jest kwadratowa
    for row in matrix:
        if len(row) != n:
            raise ValueError("Macierz nie jest kwadratowa")

    # Oblicz stopień każdego wierzchołka (ile ma sąsiadów)
    degrees = []
    for i in range(n):
        deg = sum(1 for j in range(n) if matrix[i][j] != 0 and matrix[i][j] != INF)
        degrees.append((i, deg))

    # Sortuj malejąco wg stopnia (Largest First)
    degrees.sort(key=lambda x: x[1], reverse=True)

    coloring = {}

    for v, _ in degrees:
        # Znajdź kolory sąsiadów
        used_colors = set()
        for neighbor in range(n):
            if matrix[v][neighbor] != 0 and matrix[v][neighbor] != INF and neighbor in coloring:
                used_colors.add(coloring[neighbor])
        # Przypisz najmniejszy wolny kolor
        color = 0
        while color in used_colors:
            color += 1
        coloring[v] = color

    return coloring