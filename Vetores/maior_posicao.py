print('#' * 120)
print('Programa armazena números em um array e mostra o maior número.')
print('#' * 120)

numeros = int(input('Digite quantos números que você deseja acrescentar no array.'))
array = [int(input('Digite um número para adicionar no array')) for i in range(numeros)]
# for i in range(numeros):
#     array.append(int(input('Digite um número para adicionar no array')))

maior = 0
posicao_maior = 0

for i in range(numeros):
    if array[i] > maior:
        maior = array[i]
        posicao_maior = i

# Foma simplificada de achar o maior número
print(f'O maior número do array é {max(array)}.')

print(f'O maior número é {maior} e está na posição maior {posicao_maior}')
print('Fim do programa')