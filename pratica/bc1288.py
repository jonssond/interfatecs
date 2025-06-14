# -*- coding: utf-8 -*-

def knapsack(W, pesos, valores):
    n = len(pesos)
    dp = [[0 for _ in range(W+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w - pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]


vidas = []
casos = int(input())
for _ in range(casos):
    projeteis = int(input())
    danos = []
    pesos = []
    for _ in range(projeteis):
        dano, peso = map(int, input(). split())
        danos.append(dano)
        pesos.append(peso)
    peso_canhao = int(input())
    vida_castelo = int(input())
    vida_castelo -= knapsack(peso_canhao, pesos, danos)
    vidas.append(vida_castelo)

for i in range(len(vidas)):
    if vidas[i] > 0:
        print("Falha na missao")
    else:
        print("Missao completada com sucesso")