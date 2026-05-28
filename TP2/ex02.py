# =============================================================================
# Exercício 2 – Busca exata em Trie (search)
# =============================================================================
#
# DECISÃO DE PROJETO — palavra vazia ("")
# ----------------------------------------
# Optou-se por NÃO suportar a palavra vazia como palavra válida.
# search("") retorna False porque nenhuma inserção marca o nó raiz com
# is_end=True. Caso o sistema precise aceitar a string vazia, basta chamar
# trie.insert("") antes de pesquisá-la — o comportamento já funciona
# corretamente por conta da lógica geral do método insert.
#
# REGRA QUE DIFERENCIA PREFIXO DE PALAVRA COMPLETA
# --------------------------------------------------
# Um prefixo existe na Trie quando é possível navegar pelos children caractere
# a caractere sem encontrar um nó ausente. Já uma palavra completa exige,
# adicionalmente, que o nó final tenha is_end=True. Em outras palavras:
#   - prefixo presente  → todos os nós do caminho existem
#   - palavra completa  → todos os nós existem E o último tem is_end=True
# =============================================================================

from ex01 import TrieNode, Trie   # reutiliza as classes do Exercício 1


# Adicionamos search como método à classe Trie por monkey-patch para manter
# cada exercício em seu próprio arquivo sem herança desnecessária.
# Em produção, o método estaria diretamente dentro da classe.

def search(self, word: str) -> bool:
    """Retorna True somente se 'word' é uma palavra completa na Trie.

    Percorre os nós correspondentes a cada caractere. Se qualquer caractere
    não for encontrado em children, retorna False imediatamente. Ao término
    do caminho, verifica is_end para distinguir palavra completa de prefixo.

    Args:
        word: Palavra a ser pesquisada.

    Returns:
        True se a palavra foi inserida integralmente; False caso contrário.
    """
    current = self.root
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    return current.is_end   # <— ponto crítico: prefixo ≠ palavra


Trie.search = search   # anexa o método à classe


# =============================================================================
# Testes obrigatórios
# =============================================================================

def run_tests():
    trie = Trie()
    for word in ["car", "cart", "carro", "python", "py"]:
        trie.insert(word)

    # ── Teste 1: palavra existente ───────────────────────────────────────────
    assert trie.search("car")    is True,  "FALHOU: 'car' foi inserida"
    assert trie.search("cart")   is True,  "FALHOU: 'cart' foi inserida"
    assert trie.search("carro")  is True,  "FALHOU: 'carro' foi inserida"
    assert trie.search("python") is True,  "FALHOU: 'python' foi inserida"
    print("Teste 1 PASSOU – palavras existentes retornam True")

    # ── Teste 2: palavra inexistente com prefixo existente ───────────────────
    # 'car' existe, mas 'cars' não foi inserida
    assert trie.search("cars") is False, "FALHOU: 'cars' não foi inserida"
    # 'py' existe, mas 'pyth' não foi inserida como palavra
    assert trie.search("pyth") is False, "FALHOU: 'pyth' não foi inserida como palavra"
    print("Teste 2 PASSOU – palavras com prefixo existente mas inexistentes retornam False")

    # ── Teste 3: prefixo existente que NÃO é palavra ─────────────────────────
    # 'ca' é prefixo de 'car'/'cart'/'carro', mas não foi inserida
    assert trie.search("ca") is False, "FALHOU: 'ca' é prefixo, não palavra"
    # 'c' idem
    assert trie.search("c")  is False, "FALHOU: 'c' é prefixo, não palavra"
    print("Teste 3 PASSOU – prefixos existentes que não são palavras retornam False")

    # ── Teste 4: palavra vazia (não suportada por padrão) ────────────────────
    # Conforme decisão documentada no cabeçalho, "" retorna False.
    assert trie.search("") is False, "FALHOU: string vazia não deve ser palavra"
    print("Teste 4 PASSOU – string vazia retorna False (conforme decisão de projeto)")

    # ── Teste 5: palavra completamente inexistente ────────────────────────────
    assert trie.search("java") is False, "FALHOU: 'java' nunca foi inserida"
    print("Teste 5 PASSOU – palavra sem nenhum prefixo na Trie retorna False")

    print("\nTodos os testes do Exercício 2 passaram com sucesso!")


if __name__ == "__main__":
    run_tests()