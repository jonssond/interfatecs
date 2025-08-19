testes = int(input())

respostas = []
for _ in range(testes):
    n, k = map(int, input().split())

    roda = list(range(1, n+1))
    i = 0
    while len(roda) > 1:
        i = (i + k-1) % len(roda)
        roda.pop(i)

    respostas.append(roda[0])


for i in range(len(respostas)):
    print(f"Case {i+1}: {respostas[i]}")
