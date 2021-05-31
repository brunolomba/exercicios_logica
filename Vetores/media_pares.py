print('#' * 120)
print('Programa armazena números em um array e faz a média dos núemros pares.')
print('#' * 120)

numeros = int(input('Digite quantos númros que você deseja acrescentar no array.'))
array = []
array_pares = []
contador = 0

for i in range(numeros):
    array.append(int(input('Digite um número inteiro')))

for i in array:
    if i % 2 == 0:
        array_pares.append(i)
        contador += 1

if contador == 0:
    print('Nenhum número Zero')
else:
    media_pares = sum(array_pares) / len(array_pares)
    print(f'Os números pares são {array_pares} e a média deles é {media_pares}.')




print('Fim do programa')