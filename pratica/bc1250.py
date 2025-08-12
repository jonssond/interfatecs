testes = int(input())

tiros_totais = []

for teste in range(testes):
    tiros = int(input())

    alturas_tiros = str(input())
    alturas_tiros = alturas_tiros.split()
    alturas_tiros = [int(x) for x in alturas_tiros]

    pulos = str(input())
    pulos = list(pulos)

    tiros_rodada = 0

    for i in range(tiros):
        if pulos[i] == 'J':
            if alturas_tiros[i] > 2:
                tiros_rodada += 1
        else:
            if alturas_tiros[i] < 3:
                tiros_rodada += 1

    tiros_totais.append(tiros_rodada)

for resultado in tiros_totais:
    print(resultado)



