from binary_heap import BinaryHeap

def sift_down(heap, index, size=None):
    if size is None:
        size = len(heap)

    max_idx = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and heap[left] > heap[max_idx]:
        max_idx = left
    if right < size and heap[right] > heap[max_idx]:
        max_idx = right

    if index != max_idx:
        heap[index], heap[max_idx] = heap[max_idx], heap[index]
        sift_down(heap, max_idx, size)


def extract_max(heap):
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()

    max_val = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return max_val


if __name__ == "__main__":
    print("=== Exercício 4 — Extract-Max ===\n")

    h = BinaryHeap()
    for v in [15, 8, 25, 3, 40, 12, 30]:
        h.insert(v)

    data = h.to_list()
    print("Heap inicial:", data)
    print()

    print("Removendo elementos um a um:")
    step = 1
    while data:
        val = extract_max(data)
        print(f"  Passo {step}: extraído = {val} | heap restante = {data}")
        step += 1

    print("\nHeap esvaziada com sucesso.")
    print("Complexidade de extract_max: O(log n)")