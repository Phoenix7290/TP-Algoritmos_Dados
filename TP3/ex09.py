import heapq


def dijkstra(grafo, origem):
    distancias = {v: float("inf") for v in grafo}
    distancias[origem] = 0
    predecessores = {v: None for v in grafo}
    fila = [(0, origem)]

    while fila:
        custo_atual, atual = heapq.heappop(fila)
        if custo_atual > distancias[atual]:
            continue
        for vizinho, peso in grafo[atual]:
            novo_custo = custo_atual + peso
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                predecessores[vizinho] = atual
                heapq.heappush(fila, (novo_custo, vizinho))

    return distancias, predecessores


if __name__ == "__main__":
    print("=== Exercício 9 - Menor Custo com Dijkstra ===\n")

    grafo = {
        "Berco_A":          [("Patio_1", 4), ("Patio_2", 7)],
        "Berco_B":          [("Patio_2", 3), ("Patio_3", 6)],
        "Patio_1":          [("Berco_A", 4), ("Patio_2", 2), ("Alfandega", 8)],
        "Patio_2":          [("Berco_A", 7), ("Berco_B", 3), ("Patio_1", 2), ("Patio_3", 2), ("Alfandega", 5)],
        "Patio_3":          [("Berco_B", 6), ("Patio_2", 2), ("Centro_Logistico", 4)],
        "Alfandega":        [("Patio_1", 8), ("Patio_2", 5), ("Centro_Logistico", 3)],
        "Centro_Logistico": [("Patio_3", 4), ("Alfandega", 3)],
    }

    distancias, predecessores = dijkstra(grafo, "Berco_A")

    print("Menores distâncias a partir de Berco_A:")
    for vertice, dist in sorted(distancias.items(), key=lambda x: x[1]):
        print(f"  {vertice}: {dist}")

    print("\nComplexidade: O((V + E) log V)")
    print("Cada vértice é inserido na fila de prioridade no máximo uma vez por aresta.")
    print("Cada operação de heappush/heappop custa O(log V).")