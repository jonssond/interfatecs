total_linha = int(input())
camisas = []
for _ in range(3):
    linha_camisa, lucro = map(int, input().split())
    camisas.append((linha_camisa, lucro))

tabela = [[0] * (total_linha + 1) for _ in range(4)]

print(camisas)
print(tabela)

for i in range(1, 4):
    linha_camisa, lucro = camisas[i - 1]
    for j in range(total_linha + 1):
        if linha_camisa <= j:
            tabela[i][j] = max(tabela[i - 1][j], tabela[i][i-linha_camisa] + lucro)
        else:
            tabela[i][j] = tabela[i-1][j]

print(tabela[3][total_linha])
