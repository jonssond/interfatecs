codigo1, quantidade1, valor1 = map(float, input().split())
codigo2, quantidade2, valor2 = map(float, input().split())

resultado1 = quantidade1 * valor1
resultado2 = quantidade2 * valor2
resultado = resultado1 + resultado2

print(f'VALOR A PAGAR: R$ {resultado:.2f}')