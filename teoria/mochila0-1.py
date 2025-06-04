"""
ui e pi, i = 1, ..., n; capacidade b
ui = utilidade do item
pi = peso do item
Estágio i: envolve a decisão de levar ou não o item i
Estado(i, w): quais itens de 1 a i estão na mochila de tamanho w (w = subdivisões, tamanho restante após colocar item(s))

Recusão progressiva
z(i, w): utilidade máxima da mochila com capacidade w, considerando os itens de 1 a i, para i = 1, ..., n e w <= b 

z(i, 0) = 0, i = 1, ..., n. (Condição de contorno para w = 0)
z(0, w) = 0, w >= 0. (Condição de contorno para i = 0)

z(i, w) = max{ z(i - 1, w), ui + z(i - 1, w - pi) }
z(i - 1, w) = não levar o item i
ui + z(i - 1, w - pi) = levar o item i (somente se pi <= w)

Queremos encontrar z(n, z)
"""

"""
Função padrão:

def mochila(pesos, utilidades, capacidade):
    n = len(pesos)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range (1, capacidade + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], utilidades[i-1] + dp[i-1][w - pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    itens_selecionados = []
    w = capacidade
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            itens_selecionados.append(i-1)
            w -= pesos[i-1]
    return (dp[n][capacidade], itens_selecionados[::-1])
"""

"""
    Exercício: 
Você é um especialista em marketing digital e precisa escolher quais anúncios veicular em um espaço limitado de tempo. Cada anúncio tem um custo de exibição (em segundos) e um potencial de conversão (em clientes esperados). Seu objetivo é maximizar as conversões sem exceder o tempo total disponível.

Dados:
    Tempo total disponível: 15 segundos
    Anúncios disponíveis:

Anúncio	  Duração(seg)	  Conversões Esperadas
A	        5	                10
B	        3	                6
C	        7               	15
D	        4               	8
E	        6               	12
"""

# i = anúncio
# pi = duração do anúncio
# ui = conversão do anúncio
# b = tempo total (15)
# n = número total de anúncios (5)

def select_anuncios(duracoes, conversoes, tempoTotal):
    n = len(duracoes)
    dp = [[0 for _ in range(tempoTotal+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, tempoTotal+1):
            if duracoes[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], conversoes[i-1] + dp[i-1][w-duracoes[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    selecionados = []
    w = tempoTotal
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selecionados.append(i-1)
            w -= duracoes[i-1]
    return (dp[n][tempoTotal], selecionados[::-1])


duracoes = [5, 3, 7, 4, 6]
conversoes = [10, 6, 15, 8, 12]
tempoTotal = 15

conversao_maxima, anunciosIndex = select_anuncios(duracoes, conversoes, tempoTotal)


dicionario = {0: "A", 1: "B", 2: "C", 3: "D", 5: "E"}
anuncios = []

for index in anunciosIndex:
    anuncio = dicionario.get(index)
    anuncios.append(anuncio)

print(f"Conversão máxima obtida: {conversao_maxima}")
print("Anúncios selecionados: ", " ".join(anuncios))
