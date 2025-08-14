def busca(cartas_principe, cartas_princesa) -> bool:
    cp = sorted(cartas_principe)
    pr = sorted(cartas_princesa)
    
    vitorias_possiveis = 0
    
    for carta_p in cp:
        for carta_pr in pr:
            if carta_p > carta_pr:
                vitorias_possiveis += 1
    
    usado_princesa = [False] * 3
    vitorias = 0
    
    cp_desc = sorted(cartas_principe, reverse=True)
    pr_asc = sorted(cartas_princesa)
    
    for carta_p in cp_desc:
        for i, carta_pr in enumerate(pr_asc):
            if not usado_princesa[i] and carta_p > carta_pr:
                usado_princesa[i] = True
                vitorias += 1
                break
    
    return vitorias >= 2

while True:    
    cartas = str(input())
    if cartas == "0 0 0 0 0":
        break

    cartas = [int(x) for x in cartas.split()]
    cartas_princesa = [cartas[0], cartas[1], cartas[2]]
    cartas_principe = [cartas[3], cartas[4]]
    
    pr_sorted = sorted(cartas_princesa)
    
    resultado_final = -1
    
    for possibilidade in range(1, 53):
        if possibilidade not in cartas_princesa and possibilidade not in cartas_principe:
            teste_cartas = cartas_principe + [possibilidade]
            if busca(teste_cartas, cartas_princesa):
                resultado_final = possibilidade
                break

    print(resultado_final)