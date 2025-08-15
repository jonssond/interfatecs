def make_minute(hora, minuto):
    minutagem = minuto
    hora_minuto = hora * 60
    minutagem += hora_minuto
    return minutagem

while True:
    h_inicio, m_inicio, h_final, m_final = map(int, input().split())
    validador = h_inicio + m_inicio + h_final + m_final
    if validador == 0:
        break

    descanso_minutos = 0

    if (h_final < h_inicio) or (h_final == h_inicio and m_final < m_inicio):
        dia = 24 * 60  # dia em minutos
        descanso_minutos = (dia - make_minute(h_inicio, m_inicio)) + make_minute(h_final, m_final)
    else:
        descanso_minutos = make_minute(h_final, m_final) - make_minute(h_inicio, m_inicio)
        
    print(descanso_minutos)


