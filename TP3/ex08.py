from collections import deque


def bfs_alcancaveis(grafo, origem):
    visitado = {origem}
    fila = deque([origem])
    alcancaveis = []

    while fila:
        atual = fila.popleft()
        alcancaveis.append(atual)
        for vizinho, _ in grafo[atual]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return alcancaveis


def bfs_menor_caminho(grafo, origem, destino):
    visitado = {origem}
    fila = deque([(origem, [origem])])

    while fila:
        atual, caminho = fila.popleft()
        for vizinho, peso in grafo[atual]:
            if vizinho == destino:
                return caminho + [vizinho]
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None


def custo_caminho(grafo, caminho):
    custo = 0
    for i in range(len(caminho) - 1):
        a, b = caminho[i], caminho[i + 1]
        for vizinho, peso in grafo[a]:
            if vizinho == b:
                custo += peso
                break
    return custo


if __name__ == "__main__":
    print("=== Exercício 8 - Viabilidade Operacional no Porto ===\n")

    grafo = {
        "Berco_A":          [("Patio_1", 4), ("Patio_2", 7)],
        "Berco_B":          [("Patio_2", 3), ("Patio_3", 6)],
        "Patio_1":          [("Berco_A", 4), ("Patio_2", 2), ("Alfandega", 8)],
        "Patio_2":          [("Berco_A", 7), ("Berco_B", 3), ("Patio_1", 2), ("Patio_3", 2), ("Alfandega", 5)],
        "Patio_3":          [("Berco_B", 6), ("Patio_2", 2), ("Centro_Logistico", 4)],
        "Alfandega":        [("Patio_1", 8), ("Patio_2", 5), ("Centro_Logistico", 3)],
        "Centro_Logistico": [("Patio_3", 4), ("Alfandega", 3)],
    }

    print("Áreas alcançáveis a partir de Berco_A (ignorando pesos):")
    alcancaveis = bfs_alcancaveis(grafo, "Berco_A")
    print(f"  {alcancaveis}\n")

    caminho = bfs_menor_caminho(grafo, "Berco_A", "Centro_Logistico")
    custo = custo_caminho(grafo, caminho)

    print(f"Menor caminho em número de etapas (Berco_A → Centro_Logistico):")
    print(f"  {' → '.join(caminho)}")
    print(f"  Etapas: {len(caminho) - 1}")
    print(f"  Custo total desse caminho: {custo}")

    print("\nPor que esse caminho não é necessariamente o de menor custo?")
    print("  BFS minimiza o número de arestas, não a soma dos pesos.")
    print("  Berco_A → Patio_2 → Alfandega → Centro_Logistico custa 7+5+3 = 15")
    print("  Berco_A → Patio_1 → Patio_2 → Patio_3 → Centro_Logistico custa 4+2+2+4 = 12")
    print("  O caminho de menor custo tem mais etapas — BFS não o encontraria.")
    print("  Para minimizar custo em grafos ponderados, é necessário usar Dijkstra.")