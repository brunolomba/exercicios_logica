print('#' * 120)
print('Programa que mostra os números pares de um array.')
print('#' * 120)

numeros = int(input('Digite quantos númros que você deseja acrescentar no array.'))
array = []
array_pares = []
# contagem_pares = 0

for i in range(numeros):
    array.append(int(input('Digite um número para adicionar no array')))

for pares in array:
    if pares % 2 == 0:
        array_pares.append(pares)

# EXEMPLO QUE VARIFICA OS PARE, PRINTA ELES E FAZ A CONTAGEM DE QUANTOS PARES TEM
# for pares in array:
#     if pares % 2 == 0:
#         array_pares.append(pares)
#         print(pares)
#         contagem_pares += 1

print(f'A quantidade de pares digitados foram {len(array_pares)} e os números pares são {sorted(array_pares)}')

print('Fim do programa')