    def to_mermaid(self, directed=False) -> str:
        """
        Exporta o grafo em sintaxe Mermaid.
        Evita duplicatas não-dirigidas: só emite aresta {u,v}
        se u < v (ordem lexicográfica), garantindo exatamente
        uma linha por aresta no output.
        """
        arrow = "-->" if directed else "---"
        header = "graph TD" if directed else "graph TD"
        lines = [header]
        seen = set()
        for u in sorted(self.adj):
            for v in sorted(self.adj[u]):
                key = (min(u,v), max(u,v)) if not directed else (u,v)
                if key not in seen:
                    seen.add(key)
                    lines.append(f"    {u} {arrow} {v}")
        return "\n".join(lines)