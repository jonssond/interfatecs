'''
Você foi contratado para um projeto de busca em redes e sua primeira tarefa é implementar a travessia em largura (BFS) em um grafo.

Você receberá um grafo não-direcionado, representado por uma lista de adjacências, e um vértice de partida. Sua missão é percorrer 
o grafo a partir desse vértice inicial e retornar a ordem em que cada vértice é visitado, explorando o grafo nível por nível.

Entrada:

    V: O número total de vértices no grafo.

    adj: Uma lista de listas, onde adj[i] contém todos os vértices vizinhos ao vértice i.

    start_node: O vértice inicial da travessia.

Saída:

    Uma lista de inteiros representando a sequência de vértices visitados.

Exemplo:
Entrada:

V = 5
adj = [
  [1, 2],
  [0, 3],
  [0, 4],
  [1],
  [2]
]
start_node = 0

Saída Esperada:

[0, 1, 2, 3, 4]
'''
from collections import deque

def bfs(grafo, origem):
    visitados = {origem}
    fila = deque([origem])
    ordem_visita = []
    while fila:
        no = fila.popleft()
        ordem_visita.append(no)
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)

    return ordem_visita

v = int(input())
grafo_lista = []
for _ in range(v):
    origem, destino = map(int, input().split())
    grafo_lista.append((origem, destino))

target = int(input())

grafo = {}

for origem, destino in grafo_lista:
    if origem in grafo:
        grafo[origem].append(destino)
    else:
        grafo[origem] = [destino]

    if destino in grafo:
        grafo[destino].append(origem)
    else:
        grafo[destino] = [origem]


if target not in grafo:
    print("Este valor não está no grafo")
else:
    resultado = bfs(grafo, target)
    if resultado == []:
        print("Não há por onde percorrer")
    else:
        print(f"Ordem de visita: {resultado}")