class BinaryHeap:
    """
    Implementação de Max-Heap Binária usando lista (array).

    Invariantes:
    1. Estrutural: árvore binária quase completa (garantida pela representação em array).
    2. De ordem: todo nó pai possui valor >= que seus filhos (propriedade Max-Heap).
    """

    def __init__(self):
        """Inicializa heap vazia."""
        self.data = []

    # ==================== Funções auxiliares de índice ====================

    def _parent(self, i: int) -> int:
        """Retorna índice do pai."""
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        """Retorna índice do filho esquerdo."""
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        """Retorna índice do filho direito."""
        return 2 * i + 2

    # ==================== Invariantes da Heap ====================

    def _is_valid_heap(self) -> bool:
        """
        Verifica se a estrutura respeita as invariantes da Max-Heap:
        1. É uma árvore binária quase completa (garantido pela representação em array)
        2. Propriedade de heap: todo pai >= filhos
        """
        for i in range(1, len(self.data)):
            parent = self._parent(i)
            if self.data[i] > self.data[parent]:
                return False
        return True

    def size(self) -> int:
        """Retorna quantidade de elementos na heap."""
        return len(self.data)

    def is_empty(self) -> bool:
        return self.size() == 0

    def peek(self):
        """Retorna o maior elemento sem remover."""
        if self.is_empty():
            raise IndexError("Heap vazia")
        return self.data[0]

    # ==================== Inserção com Sift-Up ====================

    def insert(self, valor):
        """
        Insere um valor na heap mantendo a propriedade de Max-Heap.
        Registra cada troca realizada (sift-up).
        """
        self.data.append(valor)
        print(f"Inserindo {valor} na posição {len(self.data)-1}")
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, i: int):
        """Sobe o elemento até sua posição correta (bubble up)."""
        while i > 0:
            parent = self._parent(i)
            if self.data[i] > self.data[parent]:
                print(f"  Troca: {self.data[i]} (pos {i}) <-> {self.data[parent]} (pos {parent})")
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    # ==================== Método auxiliar para debug ====================

    def __str__(self):
        return f"BinaryHeap({self.data})"

    def to_list(self):
        """Retorna cópia da lista interna (útil para testes)."""
        return self.data[:]