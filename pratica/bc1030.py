# -*- coding: utf-8 -*-

testes = int(input())
for _ in range(testes):
    pessoas, salto = list(map(int, input().split()))
    lista = [1 for _ in range(pessoas)]
    personsAlive = pessoas
    i = 0
    while personsAlive != 1:
        target = i + salto - 1  #target = 1     target = 3      target = 5      target = 1
        if target >= len(lista):
            dif = target - len(lista)                           #dif = 0
            target = 0 + dif                                    #target = 0
        while lista[target] == 0:
            target += 1                                                         # target 2
        if lista[target] == 1: 
            i = target + 1      # i = 2          i = 4          i = 1
            lista[target] = 0   # 1 morreu       3 morreu       0 morreu
            personsAlive -= 1
        print(lista)
    print(lista)
    
    