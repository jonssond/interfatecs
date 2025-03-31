# -*- coding: utf-8 -*-

#Wrong answer (100%)

loops = int(input())
ondas = list(map(int, input().split()))[:loops]

picos = 0
for i in range(loops):
    anterior = ondas[i - 1] if i > 0 else ondas[-1]
    proximo = ondas[i + 1] if i < loops - 1 else ondas[0]
    atual = ondas[i]
    if (atual > anterior and atual > proximo) or (atual < anterior and atual < proximo):
        picos += 1
print(picos)