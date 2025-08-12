total = int(input())

entradas = []

for _ in range(total):
    entrada = int(input())
    entradas.append(entrada)

entradas = sorted(entradas)

dicionario = {}
ultima_entrada = None
for entrada in entradas:
    ultima_entrada = entrada
    if entrada in dicionario:
        if entrada == ultima_entrada:
            dicionario[entrada] += 1
    else:
        dicionario[entrada] = 1

for valor in dicionario:
    print(f"{valor} aparece {dicionario[valor]} vez(es)")