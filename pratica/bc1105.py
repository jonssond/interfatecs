respostas_finais = []
while True:
    respostas_parcial = []
    
    bancos, debentures = map(int, input().split())
    if bancos == 0 and debentures == 0:
        for resposta in respostas_finais:
            print(resposta)
        break
    
    reserva_input = str(input())
    reservas = reserva_input.split()
    reservas = [int(x) for x in reservas]
    
    for _ in range(debentures):
        devedor, credor, valor = map(int, input().split())
        reservas[devedor-1] = reservas[devedor-1] - valor
        reservas[credor-1] = reservas[credor-1] + valor
    
    for reserva in reservas:
        if reserva < 0:
            respostas_parcial.append('N')
        else:
            respostas_parcial.append('S')
        
    if ('N' in respostas_parcial):
        respostas_finais.append('N')
    else:
        respostas_finais.append('S')