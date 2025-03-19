def buscaBinaria(lista, num):
    indiceInicial = 0
    indiceFinal = len(lista) - 1
    while indiceInicial <= indiceFinal:
        indice = round((indiceFinal + indiceInicial) / 2)
        if lista[indice] == num:
            print("valor encontrado na posição: ", indice)
            return indice
        elif num > lista[indice]:
            indiceInicial = indice + 1
        elif num < lista[indice]:
            indiceFinal = indice - 1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
buscaBinaria(lista, 32)
