from binary_heap import BinaryHeap
import random

def test_heap():
    print("=== Testes da BinaryHeap (Exercício 3) ===\n")

    heap = BinaryHeap()

    print("Teste 1 - Inserções em ordem crescente:")
    for x in [10, 20, 30, 40, 50]:
        heap.insert(x)
    print("Heap após inserções:", heap)
    print("Válida?", heap._is_valid_heap())
    print("Maior elemento:", heap.peek(), "\n")

    heap2 = BinaryHeap()
    print("Teste 2 - Inserções aleatórias:")
    valores = [15, 8, 25, 3, 40, 12, 30]
    for v in valores:
        heap2.insert(v)
    print("Heap final:", heap2)
    print("Válida?", heap2._is_valid_heap())
    print("Tamanho:", heap2.size(), "\n")

    heap3 = BinaryHeap()
    nums = list(range(1, 21))
    random.shuffle(nums)
    print("Teste 3 - Heap com 20 elementos aleatórios")
    print("Sequência inserida:", nums)
    for n in nums:
        heap3.insert(n)
    print("Válida?", heap3._is_valid_heap())
    print("Maior elemento correto (deve ser 20)?", heap3.peek() == 20)

if __name__ == "__main__":
    test_heap()