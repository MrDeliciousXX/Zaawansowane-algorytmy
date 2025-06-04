def AlgorytmKolorowaniaWierzcholkowSLF(matrix: list[list[int]], INF=float('inf')):
    # Walidacja macierzy kwadratowej
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Macierz nie jest kwadratowa")

    # Tworzymy graf jako słownik sąsiedztwa
    graph = {}
    for i in range(n):
        neighbors = set()
        for j in range(n):
            if i != j and matrix[i][j] != INF:
                neighbors.add(j)
        graph[i] = neighbors

    import heapq

    graph_copy = {v: set(neigh) for v, neigh in graph.items()}
    degrees = {v: len(neigh) for v, neigh in graph.items()}
    removed = set()
    order = []

    heap = [(deg, v) for v, deg in degrees.items()]
    heapq.heapify(heap)

    while len(order) < n:
        while heap:
            deg, v = heapq.heappop(heap)
            if v not in removed and degrees[v] == deg:
                break
        else:
            remaining = set(range(n)) - removed
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

    # Kolorujemy w kolejności usuwania (nie odwracamy)
    coloring = {}
    for v in order:
        used_colors = {coloring[nbr] for nbr in graph[v] if nbr in coloring}
        color = 1
        while color in used_colors:
            color += 1
        coloring[v] = color

    return coloring