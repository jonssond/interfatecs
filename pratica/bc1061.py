inicio_dia = int(input().split()[1])
horas_inicio, minutos_inicio, segundos_inicio = map(int, input().split(" : "))

final_dia = int(input().split()[1])
horas_final, minutos_final, segundos_final = map(int, input().split(" : "))

inicio_em_segundos = (inicio_dia * 24 * 60 * 60) + (horas_inicio * 60 * 60) + (minutos_inicio * 60) + segundos_inicio
final_em_segundos = (final_dia * 24 * 60 * 60) + (horas_final * 60 * 60) + (minutos_final * 60) + segundos_final

diferenca_em_segundos = final_em_segundos - inicio_em_segundos


minutos = diferenca_em_segundos // 60
resto_s = diferenca_em_segundos % 60

horas = minutos // 60
if horas > 0:
    resto_m = minutos % 60
    minutos = resto_m

dias = 0

if horas >= 24:
    dias = horas // 24
    horas = horas % 24

print(f"""{dias} dia(s)
{horas} hora(s)
{minutos} minuto(s)
{resto_s} segundo(s)""")