# -*- coding: utf-8 -*-

#1. Formatação ------------------------------------------------
print("Formatação ---------------------------------------------\n")


    # .upper (converte texto para maiúsculo)
print("fatec".upper())

    #.lower (converte texto para minúsculo)
print("FATEC".lower())

    # .capitalize (primeira letra maiúscula)
print("turma do bairro".capitalize())

    # .title (primeira letra de cada palavra maiúscula)
print("turma do bairro".title())

    # f"{variável} string" (criar uma string dinâmica)
time, instituicao = "turma do bairro", "fatec"
print(f"{time} da faculdade {instituicao}")



#2. Busca ----------------------------------------------------
print("\nBusca -------------------------------------------------\n")


    # .find (retorna a posição da substring ou -1 se não achar)
print("interfatecs".find("fatecs"))

    # .index (retorna a posição e uma excessão se não achar)
print("interfatecs".index("fatecs"))

        # Na maioria dos casos vamos usar .find provavelmente

    # .startswith (verifica se a string começa com...)
print("interfatecs".startswith("inter"))
print("interfatecs".startswith("turma"))

    # .endswith (verifica se a string termina com...)
print("interfatecs".endswith("fatecs"))
print("interfatecs".endswith("bairro"))

    # .count (conta ocorrências de uma substring)
print("interfatecs".count("e"))



#3. Divisão e Junção  ----------------------------------------
print("\nDivisão e Junção --------------------------------------\n")


    # .split (divide uma string em uma lista com base no separador)
palavras = "turma_do_bairro".split("_")
for palavra in palavras:
    print(palavra.capitalize())

    # .join (junta uma lista de strings usando um separador)
time = ["turma", "do", "bairro"]
print("-".join(time))
print("".join(time))



#4. Substituição e Limpeza ------------------------------------
print("\nSubstituição e Limpeza ---------------------------------\n")


    # .replace (substitui todas as ocorrências de uma substring)
fatec = "interfatecs"
print(fatec.replace("inter", "faculdade ").replace("s", ""))

    # .strip (remove um caractere no início ou final com base no parâmetro)
    # .lstring (remove caractere na esquerda) / .rstring (remove caractere na direta)
fatec = "   inter fatecs   "
print(fatec.strip(" "))

print("objeto".lstrip("o"))
print("objeto".rstrip("o"))
print("objeto".strip("o"))

    # str.maketrans + translate (substitui vários caracteres)
criptografado = "zenit"
descriptografado = "polar"
criptografia = str.maketrans(criptografado, descriptografado)
print("zenit")




#5. Verificação de conteúdo ---------------------------------
print("\nVerificação de conteúdo ------------------------------\n")


    # .isalpha (verifica se tudo é letra)
print("fatec".isalpha())
print("fatec1".isalpha())

    # .isdigit (verifica se tudo é número)
print("123456".isdigit())
print("123456?".isdigit())

    # .isalnum (verifica se é alfanumérico)

print("turm4d0b4irr0".isalnum())
print("turm4 d0 b4irr0".isalnum())