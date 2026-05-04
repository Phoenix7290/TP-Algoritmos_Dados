from binary_heap import BinaryHeap
from ex04 import sift_down

def delete(heap, valor):
    """
    Remove a primeira ocorrência de 'valor' da heap.
    Estratégia:
      1. Localiza o índice do valor.
      2. Substitui pelo último elemento do array.
      3. Restaura a propriedade de heap: sift-up se o novo valor é maior
         que o pai, sift-down caso contrário.
    Complexidade: O(n) para localizar + O(log n) para restaurar = O(n).
    """
    try:
        idx = heap.index(valor)
    except ValueError:
        print(f"  Valor {valor} não encontrado na heap.")
        return

    last_val = heap.pop()

    if idx < len(heap):
        heap[idx] = last_val

        parent_idx = (idx - 1) // 2

        if idx > 0 and heap[idx] > heap[parent_idx]:
            while idx > 0:
                p = (idx - 1) // 2
                if heap[idx] > heap[p]:
                    heap[idx], heap[p] = heap[p], heap[idx]
                    idx = p
                else:
                    break
        else:
            sift_down(heap, idx)

    print(f"  Deletado {valor} | heap resultante: {heap}")


if __name__ == "__main__":
    print("=== Exercício 6 — delete (remoção arbitrária) ===\n")

    h = BinaryHeap()
    for v in [15, 8, 25, 3, 40, 12, 30]:
        h.insert(v)

    data = h.to_list()
    print("Heap inicial:", data)
    print()

    print("Removendo valores existentes:")
    delete(data, 25)
    delete(data, 3)
    delete(data, 40)

    print()
    print("Tentando remover valor inexistente:")
    delete(data, 99)

    print()
    print("Heap final válida?", all(
        data[(i-1)//2] >= data[i] for i in range(1, len(data))
    ))