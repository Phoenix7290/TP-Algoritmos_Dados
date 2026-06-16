from collections import deque


def menor_caminho_bfs(grafo, origem, destino):
    visitado = {origem}
    fila = deque([(origem, [origem])])

    while fila:
        atual, caminho = fila.popleft()
        for vizinho in grafo[atual]:
            if vizinho == destino:
                return caminho + [vizinho]
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None


if __name__ == "__main__":
    print("=== Exercício 6 - Menor Caminho em Rede Social ===\n")

    grafo = {
        "Idris": ["Kamil", "Talia"],
        "Kamil": ["Idris", "Lina"],
        "Talia": ["Idris", "Ken"],
        "Lina": ["Kamil", "Sasha"],
        "Sasha": ["Lina", "Marco"],
        "Marco": ["Sasha", "Ken"],
        "Ken": ["Marco", "Talia"],
    }

    caminho = menor_caminho_bfs(grafo, "Idris", "Lina")

    print(f"Caminho mínimo entre Idris e Lina:")
    print(f"  {' → '.join(caminho)}")
    print(f"  Distância: {len(caminho) - 1} conexões")

    print("\nTodos os caminhos possíveis entre Idris e Lina:")
    print("  Idris → Kamil → Lina              (2 arestas) ← mínimo")
    print("  Idris → Talia → Ken → Marco → Sasha → Lina  (5 arestas)")

    print("\nPor que o caminho é mínimo?")
    print("  BFS explora camada por camada, em ordem crescente de distância.")
    print("  O primeiro momento que o destino é encontrado, ele foi atingido")
    print("  pelo menor número possível de arestas — qualquer outro caminho")
    print("  passaria por mais etapas, pois BFS já teria visitado essas camadas antes.")