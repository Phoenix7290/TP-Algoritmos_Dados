from collections import deque


def dfs_dirigido(grafo, inicio):
    visitado = set()
    ordem = []

    def dfs(v):
        visitado.add(v)
        ordem.append(v)
        for vizinho in grafo.get(v, []):
            if vizinho not in visitado:
                dfs(vizinho)

    dfs(inicio)
    return ordem


def bfs_dirigido(grafo, inicio):
    visitado = {inicio}
    fila = deque([inicio])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return ordem


if __name__ == "__main__":
    print("=== Exercício 7 - Travessia em Grafo Direcionado ===\n")

    grafo = {
        "Inicio": ["A", "B"],
        "A": ["C"],
        "B": ["C", "F"],
        "C": ["D"],
        "D": ["E"],
        "F": ["E"],
        "E": [],
    }

    ordem_dfs = dfs_dirigido(grafo, "Inicio")
    ordem_bfs = bfs_dirigido(grafo, "Inicio")

    print("Ordem DFS:", " → ".join(ordem_dfs))
    print("Ordem BFS:", " → ".join(ordem_bfs))

    print("\n--- Comparação ---")
    print("DFS: Inicio → A → C → D → E → B → F")
    print("  Mergulha pelo primeiro filho (A), desce até o fim (E),")
    print("  só então volta para explorar B e F.")
    print()
    print("BFS: Inicio → A → B → C → F → D → E")
    print("  Visita primeiro os vizinhos diretos de Inicio (A e B),")
    print("  depois os filhos deles (C e F), e por último D e E.")
    print()
    print("Influência da direção das arestas:")
    print("  E tem arestas entrando (de D e de F), mas nenhuma saindo.")
    print("  Então E só é alcançado por quem chega a D ou F — nunca como ponto de partida.")
    print("  Da mesma forma, C só é alcançado via A ou B, nunca diretamente de Inicio.")
    print()
    print("Complexidade: O(V + E) para ambos.")
    print("Cada vértice é enfileirado/empilhado uma vez e cada aresta percorrida uma vez.")