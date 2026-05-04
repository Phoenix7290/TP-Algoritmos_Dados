from binary_heap import BinaryHeap

def contains(heap, valor):
    """
    Verifica se um valor existe na heap.
    Algoritmo: busca linear — percorre todos os elementos do array.
    Complexidade: O(n) — a heap não garante nenhuma ordenação entre subárvores
    irmãs, impossibilitando podas como em BSTs.
    """
    for item in heap:
        if item == valor:
            return True
    return False


if __name__ == "__main__":
    print("=== Exercício 5 — contains (busca linear) ===\n")

    h = BinaryHeap()
    valores = [15, 8, 25, 3, 40, 12, 30]
    for v in valores:
        h.insert(v)

    data = h.to_list()
    print("Heap:", data)
    print()

    buscas = [25, 99, 3, 0, 40]
    for b in buscas:
        resultado = contains(data, b)
        print(f"  contains({b}) -> {resultado}")

    print()
    print("Por que a heap é ruim para buscas frequentes?")
    print("  A propriedade de heap garante apenas que o pai >= filhos.")
    print("  Não há relação de ordem entre filhos esquerdo e direito,")
    print("  nem entre subárvores de mesmo nível. Portanto, não é possível")
    print("  descartar metades da árvore como em uma BST.")
    print("  Resultado: toda busca é O(n) — equivalente a varrer um array não ordenado.")