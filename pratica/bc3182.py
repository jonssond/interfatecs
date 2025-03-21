pessoas, orcamento, hoteis, fds = map(int, input().split())

lista_valores = []

for i in range(hoteis):
    custo_dia = int(input())
    min_camas = 1000
    lista_camas = list(map(int, input().split()))
    for camas in lista_camas:
        if camas < pessoas:
            continue
        min_camas = min(min_camas, camas)
    if min_camas != 1000:
        custo_total = pessoas * custo_dia
        lista_valores.append(custo_total)

if len(lista_valores) == 0:
    print("stay home")
else:
    menor_valor = min(lista_valores)
    if menor_valor > orcamento:
        print("stay home")
    else:
        print(menor_valor)
