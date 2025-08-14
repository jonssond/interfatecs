def get_last_item(current_item, passos, lista):
    print(f"lista analisada: {lista}")
    if len(lista) == 1:
        return lista[0]
    
    else:
        index_removido = lista.index(current_item)
        print(index_removido)
        nova_lista = lista.remove(current_item)
        print(nova_lista)
        if lista.index(index_removido + passos) > len(lista):
            print("Índice do próximo item é maior que a lista")
            current_item = passos - (len(lista) - index_removido)
            print(f"Novo índice a buscar: {current_item}")
            get_last_item(current_item, passos, nova_lista)
        else:
            print("Índice do próximo item está na lista")
            current_item = lista[index_removido + passos]
            print(f"Novo item removido: {current_item}")
            nova_lista = lista.remove(current_item)
            print(f"Nova lista: {nova_lista}")
            get_last_item(current_item, passos, nova_lista)


def busca(regioes):
    passos = 1
    while True:
        lista = [regiao for regiao in range(1, regioes + 1)]
        resultado = get_last_item(1, passos, lista)
        if resultado == regioes:
            return passos
        else:
            passos += 1


while True:
    regioes = int(input())
    if regioes == 0:
        break

    print(busca(regioes))

