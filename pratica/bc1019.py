entrada_s = int(input())

minutos = entrada_s // 60
resto_s = entrada_s % 60

horas = minutos // 60
if horas > 0:
    resto_m = minutos % 60
    minutos = resto_m

print(f'{horas}:{minutos}:{resto_s}')