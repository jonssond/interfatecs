import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True    

while True:
    n = int(input())
    if n == 0:
        break

    pessoas = list(range(1, n+1))

    primos = [2]
    rodada = 0
    i = 0

    while len(pessoas) > 1:
        rodada += 1
        teste = primos[len(primos)-1] + 1
        while len(primos) != rodada:
            if isPrime(teste) == True:
                primos.append(teste)
            teste += 1

        k = primos[rodada-1]
        i = (i + k-1) % len(pessoas)
        removido = pessoas.pop(i)
    print(pessoas[0])