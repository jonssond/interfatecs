# -*- coding: utf-8 -*-

#Wrong answer (100%) 

integrantes = int(input())
notas = list(map(int, input().split()))[:integrantes]

total = sum(notas)
if total % integrantes != 0:
    print(-1)

else:
    media = total // integrantes

    compassos = 1
    for nota in notas:
        if nota > media:
            compassos += nota - media
    print(compassos)