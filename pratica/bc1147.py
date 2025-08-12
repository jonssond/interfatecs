letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lista_possibilidades = []

while True:
    cavalo = str(input())
    if cavalo == '0':
        for i in range(len(lista_possibilidades)):
            print(f"Caso de Teste #{i + 1}: {lista_possibilidades[i]} movimento(s).")
        break

    movimentos_cavalo = []

    cavalo = list(cavalo)
    cavalo = tuple(cavalo)

    numerico, alfa = cavalo
    numerico = int(numerico)
    if numerico < 7 and letras.index(alfa) < 7: # top right
        numerico_novo = numerico + 2
        alfa_novo = letras[letras.index(alfa) + 1]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico < 8 and letras.index(alfa) < 6: # right top
        numerico_novo = numerico + 1
        alfa_novo = letras[letras.index(alfa) + 2]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico > 1 and letras.index(alfa) < 6: # right bottom
        numerico_novo = numerico - 1
        alfa_novo = letras[letras.index(alfa) + 2]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico > 2 and letras.index(alfa) < 7: # bottom right
        numerico_novo = numerico - 2
        alfa_novo = letras[letras.index(alfa) + 1]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico > 2 and letras.index(alfa) > 0: # bottom left
        numerico_novo = numerico - 2
        alfa_novo = letras[letras.index(alfa) - 1]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico > 1 and letras.index(alfa) > 1: # left bottom
        numerico_novo = numerico - 1
        alfa_novo = letras[letras.index(alfa) - 2]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico < 8 and letras.index(alfa) > 1: # left top
        numerico_novo = numerico + 1
        alfa_novo = letras[letras.index(alfa) - 2]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)
    if numerico < 7 and letras.index(alfa) > 0: # top left
        numerico_novo = numerico + 2
        alfa_novo = letras[letras.index(alfa) - 1]
        movimento = f"{numerico_novo}{alfa_novo}"
        movimentos_cavalo.append(movimento)


    peoes = []
    casas_atacadas = []
    for _ in range(8):
        peao = str(input())
        peao = list(peao)
        peao = tuple(peao)
        peoes.append(peao) 

    for numerico, alfa in peoes:
        numerico = int(numerico)
        if numerico > 1 and letras.index(alfa) > 0:
            numerico_novo = numerico - 1
            alfa_novo = letras[letras.index(alfa) - 1]
            casa_atacada = f"{numerico_novo}{alfa_novo}"
            casas_atacadas.append(casa_atacada)
        if numerico > 1 and letras.index(alfa) < 7:
            numerico_novo = numerico - 1
            alfa_novo = letras[letras.index(alfa) + 1]
            casa_atacada = f"{numerico_novo}{alfa_novo}"
            casas_atacadas.append(casa_atacada)

    possibilidades = 0
    for movimento_cavalo in movimentos_cavalo:
        if movimento_cavalo not in casas_atacadas:
            possibilidades += 1
    
    lista_possibilidades.append(possibilidades)
