#Prim
def AlgorytmWyznaczaniaDrzewaSpinajacego(matrix: list[list[float]], INF=float('inf')):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Macierz nie jest kwadratowa")

    visited = set([0])  # startujemy od wierzchołka 0
    edges = []
    total_weight = 0

    while len(visited) < n:
        min_edge = (None, None, INF)
        for u in visited:
            for v in range(n):
                w = matrix[u][v]
                if v not in visited and w != INF and w < min_edge[2]:
                    min_edge = (u, v, w)
        if min_edge[0] is None:
            break  # graf niespójny
        edges.append(min_edge)
        total_weight += min_edge[2]
        visited.add(min_edge[1])

    return edges, total_weight
