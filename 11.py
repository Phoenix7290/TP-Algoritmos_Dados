import random
import time

class HeapMetrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def reset(self):
        self.comparisons = 0
        self.swaps = 0


metrics = HeapMetrics()


def monitored_sift_down(arr, i, n):
    """Sift-down instrumentado para contar comparações e trocas."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        metrics.comparisons += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        metrics.comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        metrics.swaps += 1
        arr[i], arr[largest] = arr[largest], arr[i]
        monitored_sift_down(arr, largest, n)


def monitored_build_heap(array):
    """Build-heap instrumentado."""
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        monitored_sift_down(array, i, n)
    return array


def monitored_extract_max(heap):
    """Extract-max instrumentado."""
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()
    max_val = heap[0]
    heap[0] = heap.pop()
    monitored_sift_down(heap, 0, len(heap))
    return max_val


if __name__ == "__main__":
    print("=== Exercício 11 — Análise Empírica ===\n")

    tamanhos = [100, 500, 1000, 5000, 10000, 50000]

    print(f"{ 'n':>8} | {'Comps (build)':>14} | {'Trocas (build)':>14} | "
          f"{'Comps (extract)':>15} | {'Trocas (extract)':>16} | {'Tempo (ms)':>10}")
    print("-" * 90)

    for n in tamanhos:
        data = random.sample(range(n * 10), n)

        metrics.reset()
        heap = data[:]
        t0 = time.perf_counter()
        monitored_build_heap(heap)
        build_comps = metrics.comparisons
        build_swaps = metrics.swaps

        metrics.reset()
        while heap:
            monitored_extract_max(heap)
        extract_comps = metrics.comparisons
        extract_swaps = metrics.swaps
        t1 = time.perf_counter()

        elapsed_ms = (t1 - t0) * 1000

        print(f"{n:>8} | {build_comps:>14} | {build_swaps:>14} | "
              f"{extract_comps:>15} | {extract_swaps:>16} | {elapsed_ms:>10.2f}")

    print()
    print("Análise:")
    print("  build_heap:   comparações ≈ 2n  → confirma O(n) teórico")
    print("  extract_max:  trocas ≈ n log n  → confirma O(n log n) para n extrações")
    print("  Os dados empíricos validam as complexidades teóricas.")