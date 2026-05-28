class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _collect_words(self, node, prefix) -> list[str]:
        """Coleta todas as palavras na subárvore de node."""
        results = []
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            results.extend(self._collect_words(child, prefix + ch))
        return results

    def _find_node(self, prefix) -> TrieNode | None:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node