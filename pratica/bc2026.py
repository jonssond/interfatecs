# -*- coding: utf-8 -*-

def knapsack(W, pesos, valores):
    n = len(pesos)
    dp = [[0 for _ in range(W+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w-pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]


respostas = []
galhos = int(input())

for _ in range(galhos):
    pacotes = int(input())
    capacidade = int(input())

    enfeites = []
    pesos = []

    for _ in range(pacotes):
        enfeite, peso = map(int, input().split())
        enfeites.append(enfeite)
        pesos.append(peso)

    resposta = knapsack(capacidade, pesos, enfeites)
    respostas.append(resposta)

for i in range(1, galhos+1):
    print(f"Galho {i}:")
    print(f"Numero total de enfeites: {respostas[i-1]}")
    print()