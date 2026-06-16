class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.pai[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

    def conectado(self, a, b):
        return self.find(a) == self.find(b)


def processar_operacoes(N, operacoes):
    uf = UnionFind(N)
    respostas = []
    for tipo, a, b in operacoes:
        if tipo == 1:
            uf.union(a, b)
        else:
            respostas.append(1 if uf.conectado(a, b) else 0)
    return respostas


if __name__ == "__main__":
    print("=== Exercício 3 - Conectividade Dinâmica ===\n")

    N1 = 5
    operacoes1 = [
        (1, 1, 2),
        (1, 3, 4),
        (0, 1, 2),
        (0, 1, 3),
        (1, 2, 3),
        (0, 1, 4),
        (0, 1, 5),
    ]
    respostas1 = processar_operacoes(N1, operacoes1)
    print(f"Teste 1 - N={N1}")
    print(f"Operações: {operacoes1}")
    print(f"Respostas: {respostas1}")
    print(f"Esperado:  [1, 0, 1, 0]\n")

    N2 = 4
    operacoes2 = [
        (0, 1, 4),
        (1, 1, 2),
        (1, 2, 3),
        (1, 3, 4),
        (0, 1, 4),
    ]
    respostas2 = processar_operacoes(N2, operacoes2)
    print(f"Teste 2 - N={N2}")
    print(f"Operações: {operacoes2}")
    print(f"Respostas: {respostas2}")
    print(f"Esperado:  [0, 1]\n")

    print("Complexidade: O(M * α(N))")
    print("α é a inversa de Ackermann, praticamente constante.")
    print("Union-Find com path compression e union by rank é quase O(1) por operação.")