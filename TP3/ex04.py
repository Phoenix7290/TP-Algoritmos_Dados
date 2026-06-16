def dfs_recomendacoes(grafo, inicio):
    visitado = set()
    ordem = []

    def dfs(v):
        visitado.add(v)
        ordem.append(v)
        for vizinho in sorted(grafo[v]):
            if vizinho not in visitado:
                dfs(vizinho)

    dfs(inicio)
    return ordem


if __name__ == "__main__":
    print("=== Exercício 4 - DFS em Rede de Recomendações ===\n")

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

    ordem = dfs_recomendacoes(grafo, "nails")

    print("Ordem de visita a partir de 'nails':")
    for i, produto in enumerate(ordem, 1):
        print(f"  {i}. {produto}")

    print(f"\nTotal de produtos visitados: {len(ordem)}")
    print("\nComplexidade: O(V + E)")
    print("Cada vértice é visitado uma vez e cada aresta percorrida no máximo duas vezes.")