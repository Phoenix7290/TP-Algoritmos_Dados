from collections import deque


def bfs_recomendacoes(grafo, inicio):
    visitado = {inicio}
    fila = deque([inicio])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)
        for vizinho in sorted(grafo[atual]):
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return ordem


if __name__ == "__main__":
    print("=== Exercício 5 - BFS em Rede de Recomendações ===\n")

    grafo = {
        "brush": ["nail_polish"],
        "nail_polish": ["brush", "eye_shadow", "nails"],
        "eye_shadow": ["nail_polish", "eye_glasses"],
        "eye_glasses": ["eye_shadow"],
        "nails": ["nail_polish", "pins", "needles", "hammer"],
        "pins": ["nails", "needles"],
        "needles": ["nails", "pins"],
        "hammer": ["nails", "drill", "saw"],
        "drill": ["hammer"],
        "saw": ["hammer", "knife"],
        "knife": ["saw", "fork", "spoon"],
        "fork": ["knife"],
        "spoon": ["knife"],
    }

    ordem_bfs = bfs_recomendacoes(grafo, "nails")
    ordem_dfs = ["nails", "hammer", "drill", "saw", "knife", "fork", "spoon",
                 "nail_polish", "brush", "eye_shadow", "eye_glasses", "needles", "pins"]

    print("Ordem BFS a partir de 'nails':")
    for i, produto in enumerate(ordem_bfs, 1):
        print(f"  {i}. {produto}")

    print(f"\nOrdem DFS (Exercício 4):")
    for i, produto in enumerate(ordem_dfs, 1):
        print(f"  {i}. {produto}")

    print("\n--- Comparação ---")
    print("BFS visita por camadas (distância crescente a partir de 'nails'):")
    print("  Nível 0: nails")
    print("  Nível 1: hammer, nail_polish, needles, pins  (vizinhos diretos)")
    print("  Nível 2: drill, saw, brush, eye_shadow        (2 passos de nails)")
    print("  Nível 3: knife, eye_glasses                   (3 passos)")
    print("  Nível 4: fork, spoon                          (4 passos)")
    print()
    print("DFS mergulha em um caminho até o fim antes de voltar:")
    print("  nails → hammer → drill → (volta) → saw → knife → fork → spoon")
    print("  Depois explora o outro lado: nail_polish → brush → eye_shadow → ...")
    print()
    print("BFS garante que cada vértice é encontrado pela menor distância possível.")
    print("DFS não garante isso; pode visitar vértices próximos por último.")
    print("\nComplexidade: O(V + E)")