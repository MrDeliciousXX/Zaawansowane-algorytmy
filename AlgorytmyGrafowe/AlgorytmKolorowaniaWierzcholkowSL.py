def AlgorytmKolorowaniaWierzcholkowSL(matrix: list[list[int]]):
    # Walidacja
    for row in matrix:
        if len(matrix) != len(row):
            raise ValueError("Macierz nie jest kwadratowa")

    import heapq

    n = len(matrix)
    # Budujemy graf w postaci słownikowej z macierzy sąsiedztwa
    graph = {i: set() for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != float('inf'):
                graph[i].add(j)

    # Kopia grafu i stopnie
    graph_copy = {v: set(neighbors) for v, neighbors in graph.items()}
    degrees = {v: len(neighbors) for v, neighbors in graph.items()}
    removed = set()
    order = []

    heap = [(deg, v) for v, deg in degrees.items()]
    heapq.heapify(heap)

    while len(order) < len(graph):
        while heap:
            deg, v = heapq.heappop(heap)
            if v not in removed:
                break
        else:
            remaining = set(graph.keys()) - removed
            if remaining:
                v = remaining.pop()
            else:
                break

        order.append(v)
        removed.add(v)

        for neighbor in graph_copy[v]:
            if neighbor not in removed:
                graph_copy[neighbor].remove(v)
                degrees[neighbor] -= 1
                heapq.heappush(heap, (degrees[neighbor], neighbor))

    # Faza kolorowania
    coloring = {}
    for v in reversed(order):
        used_colors = {coloring[n] for n in graph[v] if n in coloring}
        color = 0
        while color in used_colors:
            color += 1
        coloring[v] = color

    return coloring
