def is_valid_heap(array):
    """
    Verifica se um array representa uma Max-Heap válida.
    Algoritmo: percorre apenas os nós internos (índices 0 até n//2 - 1),
    pois os nós folha nunca têm filhos para violar a propriedade.
    Complexidade: O(n)
    """
    n = len(array)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            return False
        if right < n and array[i] < array[right]:
            return False

    return True


if __name__ == "__main__":
    print("=== Exercício 7 — is_valid_heap ===\n")

    casos = [
        ([50, 30, 40, 10, 20], True),
        ([10, 30, 40, 50], False),
        ([100], True),
        ([], True),
        ([90, 85, 80, 70, 75, 60, 65], True),
        ([90, 85, 80, 70, 75, 60, 95], False),
    ]

    for array, esperado in casos:
        resultado = is_valid_heap(array)
        status = "✓" if resultado == esperado else "✗"
        print(f"  {status} is_valid_heap({array}) -> {resultado} (esperado: {esperado})")

    print()
    print("Justificativa do algoritmo:")
    print("  Iteramos apenas sobre nós internos (índices 0 a n//2-1).")
    print("  Para cada nó, verificamos se é >= seus filhos.")
    print("  Nós folha não precisam ser checados pois não têm filhos.")
    print("  Complexidade: O(n).")