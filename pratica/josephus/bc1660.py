while True:
    inp = str(input())
    if inp == '0':
        break

    n, a, b = map(int, inp.split())

    i = 0
    vivos = n
    visitados = {}

    while True:
        i = (a*(i*i) + b) % n
        if i not in visitados:
            visitados[i] = 0
        else:
            if visitados[i] == 0:
                visitados[i] = 1
                vivos -= 1
            else:
                break

    print(vivos)
    