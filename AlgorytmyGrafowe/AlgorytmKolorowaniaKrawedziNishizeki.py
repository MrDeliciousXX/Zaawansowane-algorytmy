INF = float('inf')

def AlgorytmKolorowaniaKrawedziNishizeki(matrix: list[list[float]]):
    # Walidacja
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Macierz nie jest kwadratowa")

    # Wyciągamy listę krawędzi (u < v żeby uniknąć powtórzeń, graf nieskierowany)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != INF:
                edges.append((i, j))

    # Budujemy sąsiedztwo krawędzi i ich stopnie incydencji
    edge_neighbors = {i: set() for i in range(len(edges))}
    vertex_edges = {v: set() for v in range(n)}

    for i, (u, v) in enumerate(edges):
        vertex_edges[u].add(i)
        vertex_edges[v].add(i)

    for i, (u, v) in enumerate(edges):
        neighbors = (vertex_edges[u] | vertex_edges[v]) - {i}
        edge_neighbors[i] = neighbors

    degrees = {i: len(neigh) for i, neigh in edge_neighbors.items()}
    removed = set()
    order = []

    # Usuwamy krawędzie o najmniejszym stopniu iteracyjnie
    for _ in range(len(edges)):
        min_deg = float('inf')
        edge_to_remove = None
        for e, deg in degrees.items():
            if e not in removed and deg < min_deg:
                min_deg = deg
                edge_to_remove = e

        order.append(edge_to_remove)
        removed.add(edge_to_remove)

        for neighbor in edge_neighbors[edge_to_remove]:
            if neighbor not in removed:
                degrees[neighbor] -= 1

    # Kolorujemy krawędzie w odwrotnej kolejności
    coloring = {}
    for e in reversed(order):
        used_colors = {coloring[neighbor] for neighbor in edge_neighbors[e] if neighbor in coloring}
        color = 0
        while color in used_colors:
            color += 1
        coloring[e] = color

    # Zamiana na oryginalne krawędzie z kolorami
    edge_color_map = {edges[e]: c for e, c in coloring.items()}
    return edge_color_map