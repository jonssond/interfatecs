while True:
    n = int(input())
    if n == 0:
        break

    k = 1
    found = False
    while found == False:
        i = 0
        regioes = list(range(1, n+1))
        while len(regioes) > 1:
            regioes.pop(i)
            i = (i + k-1) % len(regioes)
        if regioes[0] == 13:
            print(k)
            found = True
            break
        k += 1

