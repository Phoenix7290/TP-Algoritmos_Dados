    def autocorrect(self, word: str) -> str | None:
        """
        Retorna 'word' se existir; caso contrário, a palavra da trie
        que compartilha o maior prefixo com 'word'.
        Desempate: menor palavra lexicograficamente.
        """
        node = self.root
        prefix = ""
        for ch in word:
            if ch not in node.children:
                break
            node = node.children[ch]
            prefix += ch
        if prefix == word and node.is_end:
            return word          # palavra correta
        candidates = self._collect_words(node, prefix)
        if not candidates:
            return None
        return sorted(candidates)[0]  # desempate lex.