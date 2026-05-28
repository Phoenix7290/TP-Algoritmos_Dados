    def autocomplete(self, prefix: str, k: int) -> list[str]:
        """
        Retorna até k sugestões lexicograficamente ordenadas.
        O(|prefix| + S·log S), onde S = nº palavras na subárvore.
        """
        node = self._find_node(prefix)
        if node is None:
            return []
        words = self._collect_words(node, prefix)
        return sorted(words)[:k]