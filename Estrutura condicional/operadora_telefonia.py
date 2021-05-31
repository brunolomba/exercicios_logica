# total_minutos = int(input('Digite quantos minutos foram gastos'))
# valor = 50
# plano = 100
# minutos_excedentes = 0
# valor_final = 0

# if 100 < total_minutos:
#     minutos_excedentes = total_minutos - plano
#     valor_final = minutos_excedentes * 2 + valor
# else:
#     valor_final = minutos_excedentes * 2 + valor

# print(f'Foram gastos {total_minutos} minutos e a a conta ficou no valor de R${valor_final}')

minutos = int(input('Digite quantos minutos foram gastos'))
valor_pago = 50

if minutos > 100:
    valor_pago = valor_pago + 2 * (minutos - 100)

print(f'Foram gastos {minutos} minutos e a a conta ficou no valor de R${valor_pago}')