import sys

def resolver():
    while True:
        try:
            linha = sys.stdin.readline()
            if not linha:
                break
            
            operacoes, caixa = map(int, linha.split())
            if operacoes == 0 and caixa == 0:
                break
            
            transacoes = [int(sys.stdin.readline()) for _ in range(operacoes)]
        except (IOError, ValueError):
            break

        soma_total = sum(transacoes)
        offset = soma_total

        dp_prefixo = [set() for _ in range(operacoes + 1)]
        dp_prefixo[0].add(offset)

        for i in range(1, operacoes + 1):
            for soma_anterior in dp_prefixo[i - 1]:
                transacao_atual = transacoes[i - 1]
                dp_prefixo[i].add(soma_anterior + transacao_atual)
                dp_prefixo[i].add(soma_anterior - transacao_atual)
        
        if (caixa + offset) not in dp_prefixo[operacoes]:
            print("*")
            continue

        dp_sufixo = [set() for _ in range(operacoes + 2)]
        dp_sufixo[operacoes + 1].add(offset)

        for i in range(operacoes, 0, -1):
            for soma_anterior in dp_sufixo[i + 1]:
                transacao_atual = transacoes[i - 1]
                dp_sufixo[i].add(soma_anterior + transacao_atual)
                dp_sufixo[i].add(soma_anterior - transacao_atual)

        resultado = []
        for i in range(operacoes):
            pode_ser_entrada = False
            pode_ser_saida = False

            caixa_necessario_entrada = caixa - transacoes[i]
            for soma_prefixo in dp_prefixo[i]:
                soma_restante = caixa_necessario_entrada - (soma_prefixo - offset)
                if (soma_restante + offset) in dp_sufixo[i + 2]:
                    pode_ser_entrada = True
                    break
            
            caixa_necessario_saida = caixa + transacoes[i]
            for soma_prefixo in dp_prefixo[i]:
                soma_restante = caixa_necessario_saida - (soma_prefixo - offset)
                if (soma_restante + offset) in dp_sufixo[i + 2]:
                    pode_ser_saida = True
                    break

            if pode_ser_entrada and pode_ser_saida:
                resultado.append("?")
            elif pode_ser_entrada:
                resultado.append("+")
            else:
                resultado.append("-")
        
        print("".join(resultado))

resolver()