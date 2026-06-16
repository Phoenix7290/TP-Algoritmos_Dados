from collections import deque


def contar_passeios_validos(S, tuneis, passeios):
    adj = {i: [] for i in range(1, S + 1)}
    for x, y in tuneis:
        adj[x].append(y)
        adj[y].append(x)

    def bfs_conectado(origem, destino):
        if origem == destino:
            return True
        visitado = {origem}
        fila = deque([origem])
        while fila:
            atual = fila.popleft()
            for viz in adj[atual]:
                if viz == destino:
                    return True
                if viz not in visitado:
                    visitado.add(viz)
                    fila.append(viz)
        return False

    validos = 0
    for passeio in passeios:
        possivel = True
        for i in range(len(passeio) - 1):
            if not bfs_conectado(passeio[i], passeio[i + 1]):
                possivel = False
                break
        if possivel:
            validos += 1

    return validos


if __name__ == "__main__":
    print("=== Exercício 2 - Validação de Passeios ===\n")

    S1 = 5
    tuneis1 = [(1, 2), (2, 3), (3, 4)]
    passeios1 = [
        [1, 3, 4],
        [1, 5],
        [2, 4, 3],
    ]
    resultado1 = contar_passeios_validos(S1, tuneis1, passeios1)
    print(f"Teste 1 - S={S1}, tuneis={tuneis1}")
    print(f"Passeios: {passeios1}")
    print(f"Passeios válidos: {resultado1}")
    print(f"Esperado: 2  (passeio [1,5] inválido, salão 5 desconectado)\n")

    S2 = 6
    tuneis2 = [(1, 2), (2, 3), (4, 5), (5, 6)]
    passeios2 = [
        [1, 2, 3],
        [4, 6],
        [1, 4],
        [5, 4, 6],
    ]
    resultado2 = contar_passeios_validos(S2, tuneis2, passeios2)
    print(f"Teste 2 - S={S2}, tuneis={tuneis2}")
    print(f"Passeios: {passeios2}")
    print(f"Passeios válidos: {resultado2}")
    print(f"Esperado: 3  (passeio [1,4] inválido, componentes separados)\n")

    print("Complexidade: O(P * N * (S + T))")
    print("P passeios, cada um com até N salões, cada BFS custa O(S + T).")