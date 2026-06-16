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


def reconstruir_caminho(predecessores, origem, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    if caminho[0] == origem:
        return caminho
    return None


if __name__ == "__main__":
    print("=== Exercício 10 - Reconstrução de Rota Ótima ===\n")

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
    caminho = reconstruir_caminho(predecessores, "Berco_A", "Centro_Logistico")

    print(f"Caminho mínimo: {' → '.join(caminho)}")
    print(f"Custo total: {distancias['Centro_Logistico']}")

    print("\nComo a reconstrução funciona:")
    print("  Dijkstra armazena, para cada vértice, qual foi seu predecessor no caminho mínimo.")
    print("  A reconstrução parte do destino e segue os predecessores em sentido reverso até a origem.")
    print("  Por fim, inverte a lista para obter a ordem correta de início ao fim.")
    print()
    print("  Rastreamento reverso:")
    atual = "Centro_Logistico"
    while atual is not None:
        proximo = predecessores[atual]
        if proximo:
            print(f"    predecessores[{atual}] = {proximo}")
        else:
            print(f"    predecessores[{atual}] = None  ← origem")
        atual = proximo