while True:
    try:    
        tamanhoCifra, testes = map(int, input().split())

        cifra1 = list(input())
        cifra2 = list(input())
        dict1 = {}
        dict2 = {}

        for i in range(tamanhoCifra):
            dict1[cifra1[i]] = cifra2[i]
            dict2[cifra2[i]] = cifra1[i]

        listaParaImprimir = []

        for teste in range(testes):
            texto = input()
            textoLista = list(texto)
            for i in range(len(textoLista)):
                if textoLista[i].upper() in dict1:
                    cifrado = dict1[textoLista[i].upper()]
                    if textoLista[i] == textoLista[i].lower():
                        textoLista[i] = cifrado.lower()
                    else:
                        textoLista[i] = cifrado
                elif textoLista[i].upper() in dict2:
                    cifrado = dict2[textoLista[i].upper()]
                    if textoLista[i] == textoLista[i].lower():
                        textoLista[i] = cifrado.lower()
                    else:
                        textoLista[i] = cifrado
            novoText = ''.join(textoLista)
            listaParaImprimir.append(novoText)
        print("\n".join(listaParaImprimir))
    except EOFError:
        break
    