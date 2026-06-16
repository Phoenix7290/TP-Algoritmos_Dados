import heapq
from collections import deque


def bfs_caminho(grafo, origem, destino):
    visitado = {origem}
    fila = deque([(origem, [origem])])

    while fila:
        atual, caminho = fila.popleft()
        for vizinho, _ in grafo[atual]:
            if vizinho == destino:
                return caminho + [vizinho]
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return None


def dijkstra_caminho(grafo, origem, destino):
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

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return caminho, distancias[destino]


def custo_real(grafo, caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        a, b = caminho[i], caminho[i + 1]
        for vizinho, peso in grafo[a]:
            if vizinho == b:
                custo += peso
                break
    return custo


if __name__ == "__main__":
    print("=== Exercício 11 - Impacto dos Pesos na Escolha de Rotas ===\n")

    grafo = {
        "Berco_A":          [("Patio_1", 4), ("Patio_2", 7)],
        "Berco_B":          [("Patio_2", 3), ("Patio_3", 6)],
        "Patio_1":          [("Berco_A", 4), ("Patio_2", 2), ("Alfandega", 8)],
        "Patio_2":          [("Berco_A", 7), ("Berco_B", 3), ("Patio_1", 2), ("Patio_3", 2), ("Alfandega", 5)],
        "Patio_3":          [("Berco_B", 6), ("Patio_2", 2), ("Centro_Logistico", 4)],
        "Alfandega":        [("Patio_1", 8), ("Patio_2", 5), ("Centro_Logistico", 3)],
        "Centro_Logistico": [("Patio_3", 4), ("Alfandega", 3)],
    }

    caminho_bfs = bfs_caminho(grafo, "Berco_A", "Centro_Logistico")
    custo_bfs = custo_real(grafo, caminho_bfs)

    caminho_dijk, custo_dijk = dijkstra_caminho(grafo, "Berco_A", "Centro_Logistico")

    print(f"Caminho BFS:     {' → '.join(caminho_bfs)}")
    print(f"Etapas: {len(caminho_bfs) - 1}  |  Custo real: {custo_bfs}\n")

    print(f"Caminho Dijkstra: {' → '.join(caminho_dijk)}")
    print(f"Etapas: {len(caminho_dijk) - 1}  |  Custo real: {custo_dijk}\n")

    print("Conclusão:")
    print(f"  BFS encontrou caminho com {len(caminho_bfs)-1} etapas e custo {custo_bfs}.")
    print(f"  Dijkstra encontrou caminho com {len(caminho_dijk)-1} etapas e custo {custo_dijk}.")
    economia = custo_bfs - custo_dijk
    print(f"  Usar Dijkstra representa uma economia de {economia} unidades de custo operacional.")
    print("  BFS trata todas as arestas como se tivessem peso 1 — o que pode ser ineficiente")
    print("  em redes reais onde os custos variam significativamente.")