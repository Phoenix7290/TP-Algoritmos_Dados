# Algoritmos Avançados — Heaps

Vídeo 1 - https://drive.google.com/file/d/1pkJElKz8GIDTbkq4EcYG1jHoxWcmw5vc/view?usp=drive_link
Coleção de exercícios e utilitários sobre heaps (Max-Heap binária). Os arquivos contêm implementações, exemplos e pequenos benchmarks para operações como insert, extract-max, build-heap e verificações.

Status
- Código: funcionalidade principal presente.
- Comentários `#` foram removidos; as docstrings foram preservadas.

Arquivos importantes
- [02.py](02.py) — implementação da classe `BinaryHeap`.
- [03.py](03.py) — testes/uso da `BinaryHeap`.
- [04.py](04.py) — `sift_down` e `extract_max` (funções utilitárias).
- [05.py](05.py) — `contains` (busca linear em heap).
- [06.py](06.py) — `delete` (remoção arbitrária de elemento em heap).
- [07.py](07.py) — `is_valid_heap` (validação estrutural).
- [08.py](08.py) — `build_heap` (algoritmo de Floyd).
- [10.py](10.py) — `get_top_k` (top-k usando heap).
- [11.py](11.py) — métricas e benchmark instrumentado.
- Notas: [01.md](01.md), [09.md](09.md), [12.md](12.md).

Como executar

Pré-requisitos: Python 3.8+.

Observação sobre imports
Alguns exemplos importam módulos por nomes como `binary_heap`, `ex04`, `ex08` enquanto os arquivos correspondentes no repositório usam nomes numéricos (por exemplo `02.py`, `04.py`, `08.py`). Para executar os exemplos sem editar os imports, crie links simbólicos com os nomes esperados:

```bash
ln -s 02.py binary_heap.py
ln -s 04.py ex04.py
ln -s 08.py ex08.py
```

Após criar os links, execute os scripts de exemplo:

```bash
python3 03.py
python3 04.py
python3 05.py
python3 06.py
python3 07.py
python3 08.py
python3 10.py
python3 11.py
```

Alternativa: renomeie os arquivos ou ajuste `PYTHONPATH`/os imports conforme preferir.

Notas finais
- README conciso e orientado a uso rápido. Posso também:
  - renomear ou adicionar módulos (`binary_heap.py`, `ex04.py`, `ex08.py`) para evitar links;
  - executar os exemplos aqui para verificar execução e corrigir import errors.


# TP 2

Vídeo - 

Prints - 

