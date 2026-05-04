def sift_down(arr, i, n):
    """Desce o elemento da posição i até sua posição correta."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, largest, n)


def build_heap(array):
    """
    Constrói uma Max-Heap a partir de um array não ordenado.
    Algoritmo de Floyd (bottom-up): começa do último nó interno
    e aplica sift-down até a raiz.
    Complexidade: O(n) — demonstrável pela soma geométrica das trocas por nível.
    """
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n)
    return array


if __name__ == "__main__":
    print("=== Exercício 8 — build_heap ===\n")

    exemplos = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [10, 20, 5, 30, 15],
        [1, 2, 3, 4, 5, 6, 7],
        [42],
        [5, 3, 8, 1, 9, 2, 7, 4, 6],
    ]

    for arr in exemplos:
        original = arr[:]
        resultado = build_heap(arr[:])
        print(f"  Original : {original}")
        print(f"  Heap     : {resultado}")
        valida = all(resultado[(i-1)//2] >= resultado[i] for i in range(1, len(resultado)))
        print(f"  Válida?  : {valida}\n")

    print("Complexidade: O(n)")
    print("A soma das alturas de todos os nós converge para O(n).")