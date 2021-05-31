print('#' * 120)
print('Programa que adicionar números reais em um array, mostra os números e depois soma.')
print('#' * 120)

quantidade_numeros = int(input('Digite a quantidade de elementos que você deseja acrescentar no array.'))
array = []
soma = 0

for i in range(quantidade_numeros):
    valor = float(input('Digite o valor desejado.'))
    array.append(valor)

for i in array:
    print(i)

for i in array:
    soma += i

media = soma / quantidade_numeros

print(f'A lista digitada foi {sorted(array)}, a soma é {soma} e a media é {media}.')

print('Fim do programa')