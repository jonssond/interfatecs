# -*- coding: utf-8 -*-

def knapsack(T, pesos, valores):
    n = len(pesos)
    dp = [0 for _ in range(T + 1)]

    for w in range(T + 1):
        for i in range(n):
            if pesos[i] <= w:
                dp[w] = max(dp[w], valores[i] + dp[w - pesos[i]])
    return dp[T]

respostas = []
while True:
    atracoes, tempoTotal = map(int, input().split())
    if atracoes == 0:
        break
    tempos = []
    pontuacoes = []
    for _ in range(atracoes):
        tempo, pontuacao = map(int, input().split())
        tempos.append(tempo)
        pontuacoes.append(pontuacao)
    res = knapsack(tempoTotal, tempos, pontuacoes)
    respostas.append(res)

for i in range(len(respostas)):
    print(f"Instancia {i + 1}")
    print(respostas[i])
    print()