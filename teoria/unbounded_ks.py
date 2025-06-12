def unbounded_knapsack(T, pesos, valores):
    n = len(pesos)
    dp = [0 for _ in range(T + 1)]
    last_used = [-1 for _ in range(T + 1)]

    for w in range(T + 1):
        for i in range(n):
            if pesos[i] <= w:
                if dp[w] < valores[i] + dp[w - pesos[i]]:
                    dp[w] = valores[i] + dp[w - pesos[i]]
                    last_used[w] = i

    item_count = [0 for _ in range(n)]
    w = T
    while w > 0 and last_used[w] != -1:
        i = last_used[w]
        item_count[i] += 1
        w -= pesos[i]

    return dp[T], item_count

'''
Exercício

Uma fábrica de suplementos alimentares quer produzir um mix de produtos que maximize a proteína total sem ultrapassar um limite de custo de produção. A empresa possui várias receitas de suplementos, cada uma com um custo de produção e uma quantidade de proteína fornecida.

Você pode produzir quantas unidades quiser de cada suplemento, desde que o custo total não ultrapasse o orçamento da fábrica.
Orçamento = R$10
Suplemento1 = R$2, proteína 6g
Suplemento2 = R$3, proteína 10g
Suplemento3 = R$5, proteína 15g
'''

orcamento = 10
custos = [2, 3, 5]
proteina = [6, 10, 15]

res = unbounded_knapsack(orcamento, custos, proteina)
print(res)

