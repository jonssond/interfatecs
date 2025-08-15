def dfs(grafo, visitados, no_atual, target, distancia):
    distancia += 1
    visitados.add(no_atual)
    for vizinho in grafo[no_atual]:
        if vizinho == target:
            return distancia
        else:
            if vizinho not in visitados:
                distancia_encontrada = dfs(grafo, visitados, vizinho, target, distancia)
                if distancia_encontrada is not None:
                    return distancia_encontrada 
    return None
    
# =======================================================================================

usuarios = int(input())

conexoes = []
for usuario in range(usuarios):
    origem, destino = map(str, input().split())
    conexoes.append((origem, destino))

usuario_comeco, usuario_final = map(str, input().split())


grafo = {}
for origem, destino in conexoes:
    if origem in grafo:
        grafo[origem].append(destino)
    else:
        grafo[origem] = [destino]
    if destino in grafo:
        grafo[destino].append(origem)
    else:
        grafo[destino] = [origem]

print(grafo)

visitados = set()
output = dfs(grafo, visitados, usuario_comeco, usuario_final, 0)

if output == None:
    print("Vizinho não encontrado")
else:
    print(f"A distância é: {output} conexões")
