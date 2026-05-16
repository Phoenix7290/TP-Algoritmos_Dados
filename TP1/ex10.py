from ex04 import extract_max
from ex08 import build_heap

def get_top_k(array, k):
    heap = array[:]
    build_heap(heap)

    top_k = []
    for _ in range(min(k, len(heap))):
        top_k.append(extract_max(heap))

    return top_k


if __name__ == "__main__":
    print("=== Exercício 10 — Heap Sort Parcial (Top-K) ===\n")

    data = [15, 3, 17, 10, 84, 19, 6, 22, 9]
    print("Array original:", data)
    print()

    for k in [1, 3, 5, len(data)]:
        resultado = get_top_k(data, k)
        print(f"  Top {k}: {resultado}")

    print()
    print("Eficiência:")
    print("  Para k=3 e n=9: O(9) + O(3 * log 9) ≈ O(9) + O(9) = O(n)")
    print("  Ordenar tudo seria O(n log n) — desnecessário quando k << n.")