import heapq
from collections import deque


def dfs(grafo, origem):
    visitado = set()
    ordem = []

    def _dfs(v):
        visitado.add(v)
        ordem.append(v)
        for vizinho, _ in grafo[v]:
            if vizinho not in visitado:
                _dfs(vizinho)

    _dfs(origem)
    return ordem


def bfs(grafo, origem):
    visitado = {origem}
    fila = deque([origem])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)
        for vizinho, _ in grafo[atual]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return ordem


def dijkstra(grafo, origem):
    distancias = {v: float("inf") for v in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]

    while fila:
        custo_atual, atual = heapq.heappop(fila)
        if custo_atual > distancias[atual]:
            continue
        for vizinho, peso in grafo[atual]:
            novo_custo = custo_atual + peso
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                heapq.heappush(fila, (novo_custo, vizinho))

    return distancias


if __name__ == "__main__":
    print("=== Exercício 12 - Análise de Rotas na Rede Logística ===\n")

    grafo = {
        "Berco_A":          [("Patio_1", 4), ("Patio_2", 7)],
        "Berco_B":          [("Patio_2", 3), ("Patio_3", 6)],
        "Patio_1":          [("Berco_A", 4), ("Patio_2", 2), ("Alfandega", 8)],
        "Patio_2":          [("Berco_A", 7), ("Berco_B", 3), ("Patio_1", 2), ("Patio_3", 2), ("Alfandega", 5)],
        "Patio_3":          [("Berco_B", 6), ("Patio_2", 2), ("Centro_Logistico", 4)],
        "Alfandega":        [("Patio_1", 8), ("Patio_2", 5), ("Centro_Logistico", 3)],
        "Centro_Logistico": [("Patio_3", 4), ("Alfandega", 3)],
    }

    ordem_dfs = dfs(grafo, "Berco_A")
    ordem_bfs = bfs(grafo, "Berco_A")
    distancias = dijkstra(grafo, "Berco_A")

    print("Ordem de visita DFS:", " → ".join(ordem_dfs))
    print("Ordem de visita BFS:", " → ".join(ordem_bfs))

    print("\nDistâncias mínimas (Dijkstra) a partir de Berco_A:")
    for vertice, dist in sorted(distancias.items(), key=lambda x: x[1]):
        print(f"  {vertice}: {dist}")

    print("\n--- Análise Comparativa ---\n")

    print("Por que DFS e BFS produzem ordens diferentes?")
    print("  DFS usa pilha implícita (recursão) e mergulha no primeiro vizinho disponível,")
    print("  explorando o grafo em profundidade antes de retornar para outras ramificações.")
    print("  BFS usa fila explícita (FIFO) e visita todos os vizinhos do nível atual")
    print("  antes de avançar, explorando camada por camada.\n")

    print("Por que BFS não considera custos?")
    print("  BFS trata cada aresta com peso igual a 1 implicitamente.")
    print("  A fila não ordena por custo acumulado, apenas por ordem de chegada.")
    print("  O primeiro caminho encontrado tem o menor número de arestas, não o menor custo.\n")

    print("Por que Dijkstra pode escolher caminhos diferentes?")
    print("  Dijkstra usa uma fila de prioridade ordenada pelo custo acumulado.")
    print("  Ele pode preferir um caminho mais longo em arestas se a soma dos pesos for menor.")
    print("  Exemplo: Berco_A → Patio_1 → Patio_2 → Patio_3 → Centro_Logistico (custo 12)")
    print("  é preferível a Berco_A → Patio_1 → Alfandega → Centro_Logistico (custo 15),")
    print("  mesmo tendo mais etapas.\n")

    print("--- Papel de cada algoritmo na rede logística ---\n")
    print("  DFS")
    print("    Quando usar: verificar se existe algum caminho entre dois pontos,")
    print("    detectar ciclos, ou explorar toda a rede sem prioridade específica.")
    print("    Limitação: não garante menor caminho nem menor custo.\n")

    print("  BFS")
    print("    Quando usar: encontrar o caminho com menor número de etapas,")
    print("    útil quando cada deslocamento tem custo idêntico (ex: tempo fixo por trecho).")
    print("    Limitação: ignora pesos — inadequado quando custos variam entre trechos.\n")

    print("  Dijkstra")
    print("    Quando usar: minimizar o custo operacional total de movimentação,")
    print("    encontrar a rota mais eficiente economicamente entre dois pontos do porto.")
    print("    Limitação: não funciona com pesos negativos; mais custoso que BFS/DFS.")