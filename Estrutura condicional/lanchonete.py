codigo = int(input('Digite o código do produto'))
quantidade = int(input('Digite a quantidade de produtos'))
valor_pago = 0

if codigo == 1:
    valor_pago = 5 * quantidade
elif codigo == 2:
    valor_pago = 3.5 * quantidade
elif codigo == 3:
    valor_pago = 4.8 * quantidade
elif codigo == 4:
    valor_pago = 8.9 * quantidade
elif codigo == 5:
    valor_pago = 7.32 * quantidade

print(f'O valor a ser pago é {valor_pago} reais')