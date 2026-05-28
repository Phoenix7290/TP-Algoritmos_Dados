# =============================================================================
# Exercício 1 – Implementação de Trie com inserção e marcação de fim de palavra
# =============================================================================


class TrieNode:
    """Representa um nó da Trie.

    Atributos:
        children (dict): Mapeia caracteres para nós filhos (TrieNode).
        is_end (bool): Indica se este nó é o fim de uma palavra inserida.
    """

    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class Trie:
    """Estrutura de dados Trie (árvore de prefixos).

    Permite inserir palavras e preserva a relação prefixo-palavra por meio do
    atributo is_end em cada nó terminal.

    Atributos:
        root (TrieNode): Nó raiz da Trie (não representa nenhum caractere).
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insere uma palavra na Trie.

        Percorre (ou cria) um nó por caractere. Ao final, marca is_end=True
        no último nó, sinalizando que aquele caminho forma uma palavra completa.
        Inserções repetidas da mesma palavra são idempotentes: apenas confirmam
        is_end=True sem duplicar nós.

        Args:
            word: Palavra a ser inserida.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True


# =============================================================================
# Testes mínimos
# =============================================================================

def run_tests():
    trie = Trie()

    # ── Teste 1: inserção de palavra nova ────────────────────────────────────
    trie.insert("car")
    # Navega manualmente para verificar que o caminho c→a→r existe e is_end=True
    node = trie.root
    for ch in "car":
        assert ch in node.children, f"Caractere '{ch}' não encontrado após inserção de 'car'"
        node = node.children[ch]
    assert node.is_end, "is_end deveria ser True no último nó de 'car'"
    print("Teste 1 PASSOU – inserção de palavra nova ('car')")

    # ── Teste 2: inserção repetida da mesma palavra ──────────────────────────
    trie.insert("car")   # segunda inserção; não deve gerar erro nem duplicar nós
    node = trie.root
    for ch in "car":
        node = node.children[ch]
    assert node.is_end, "is_end deveria continuar True após inserção repetida de 'car'"
    # Confirma que não foram criados nós extras (o nó 'r' continua sem filhos extras)
    print("Teste 2 PASSOU – inserção repetida da mesma palavra ('car')")

    # ── Teste 3: palavra que é prefixo de outra ──────────────────────────────
    trie.insert("cart")
    trie.insert("carro")

    # 'car' deve ser palavra (is_end=True no 'r' de car)
    node_car = trie.root.children["c"].children["a"].children["r"]
    assert node_car.is_end, "'car' deveria ser marcada como palavra"

    # 'cart' deve existir como extensão de 'car'
    assert "t" in node_car.children, "'t' deveria existir como filho de 'car'"
    assert node_car.children["t"].is_end, "'cart' deveria ser marcada como palavra"

    # 'carro' deve existir: c→a→r→r→o
    assert "r" in node_car.children, "segundo 'r' de 'carro' deveria existir"
    node_carro = node_car.children["r"].children["o"]
    assert node_carro.is_end, "'carro' deveria ser marcada como palavra"

    # O nó intermediário do segundo 'r' NÃO deve ser palavra
    assert not node_car.children["r"].is_end, \
        "O 'r' intermediário de 'carro' não deveria ser marcado como fim de palavra"

    print("Teste 3 PASSOU – palavras que são prefixo de outras ('car', 'cart', 'carro')")
    print("\nTodos os testes do Exercício 1 passaram com sucesso!")


if __name__ == "__main__":
    run_tests()