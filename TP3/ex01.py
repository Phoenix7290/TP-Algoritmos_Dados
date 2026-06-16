def contar_times(N, M, amizades):
    adj = {i: [] for i in range(1, N + 1)}
    for a, b in amizades:
        adj[a].append(b)
        adj[b].append(a)

    visitado = set()
    grupos = 0

    def dfs(v):
        visitado.add(v)
        for vizinho in adj[v]:
            if vizinho not in visitado:
                dfs(vizinho)

    for aluno in range(1, N + 1):
        if aluno not in visitado:
            dfs(aluno)
            grupos += 1

    return grupos


if __name__ == "__main__":
    print("=== Exercício 1 - Formação de Times ===\n")

    N1, M1 = 6, 4
    amizades1 = [(1, 2), (2, 3), (4, 5), (5, 6)]
    resultado1 = contar_times(N1, M1, amizades1)
    print(f"Teste 1 - N={N1}, M={M1}, amizades={amizades1}")
    print(f"Times formados: {resultado1}")
    print(f"Esperado: 2\n")

    N2, M2 = 5, 0
    amizades2 = []
    resultado2 = contar_times(N2, M2, amizades2)
    print(f"Teste 2 - N={N2}, M={M2}, amizades={amizades2}")
    print(f"Times formados: {resultado2}")
    print(f"Esperado: 5\n")

    N3, M3 = 4, 3
    amizades3 = [(1, 2), (2, 3), (3, 4)]
    resultado3 = contar_times(N3, M3, amizades3)
    print(f"Teste 3 - N={N3}, M={M3}, amizades={amizades3}")
    print(f"Times formados: {resultado3}")
    print(f"Esperado: 1\n")

    print("Complexidade: O(N + M)")
    print("Cada vértice e aresta é visitado no máximo uma vez pela DFS.")