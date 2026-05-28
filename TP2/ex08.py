class GraphAdjMatrix:
    def __init__(self):
        self.index: dict[str, int] = {}   # vértice → índice na matriz
        self.mat:   list[list[int]] = []  # matriz V×V de 0/1

    def add_vertex(self, v):
        if v in self.index:
            return
        n = len(self.index)
        self.index[v] = n
        for row in self.mat:     # expande cada linha existente
            row.append(0)
        self.mat.append([0] * (n + 1))  # nova linha

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        i, j = self.index[u], self.index[v]
        self.mat[i][j] = 1
        if not directed:
            self.mat[j][i] = 1

    def has_edge(self, u, v) -> bool:
        if u not in self.index or v not in self.index:
            return False
        return self.mat[self.index[u]][self.index[v]] == 1