# Vértices: serviços de uma arquitetura de microsserviços
VERTICES = [
    "auth-service", "auth-gateway", "auth-token",
    "api-gateway",  "api-router",   "api-cache",
    "user-profile", "user-session", "user-audit",
    "db-primary",   "db-replica",   "db-backup",
    "notif-email",  "notif-push",   "log-service",
]

# 1. Inserir todos na Trie
trie = Trie()
for v in VERTICES:
    trie.insert(v)

# 2. Construir grafo (lista de adjacência)
g = GraphAdjList()
ARESTAS = [
    ("api-gateway", "auth-service"), ("api-gateway", "user-profile"),
    ("api-gateway", "api-router"),   ("api-router",  "api-cache"),
    ("auth-service", "auth-gateway"), ("auth-service", "auth-token"),
    ("auth-gateway", "auth-token"),  ("user-profile", "user-session"),
    ("user-profile", "user-audit"),  ("user-session", "db-primary"),
    ("db-primary",   "db-replica"),   ("db-primary",   "db-backup"),
    ("db-replica",   "db-backup"),    ("api-gateway",  "notif-email"),
    ("notif-email",  "notif-push"),   ("api-gateway",  "log-service"),
]
for u, v in ARESTAS:
    g.add_edge(u, v)

# 3. Função de integração
def find_vertices_by_prefix(prefix: str, k: int) -> list[str]:
    """
    Usa autocomplete da trie para obter candidatos,
    depois filtra apenas vértices existentes no grafo.
    Custo: O(p + N + W·log W) — dominado pelo autocomplete.
    """
    candidates = trie.autocomplete(prefix, k * 3)  # sobreamostra
    return [c for c in candidates if c in g.adj][:k]