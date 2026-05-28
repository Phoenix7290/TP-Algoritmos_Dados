class GraphAdjList:
    def __init__(self):
        self.adj: dict[str, set] = {}  # vértice → conjunto de vizinhos

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
        if not directed:
            self.adj[v].add(u)  # não-dirigido: ambos os sentidos

# Grafo de teste: 10 vértices, 12 arestas (não-dirigido)
g = GraphAdjList()
arestas = [
    ("A","B"),("A","C"),("B","D"),("B","E"),
    ("C","F"),("C","G"),("D","H"),("E","H"),
    ("F","I"),("G","J"),("H","I"),("I","J"),
]
for u, v in arestas:
    g.add_edge(u, v)