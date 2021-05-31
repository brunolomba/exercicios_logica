print('#' * 120)
print('Programa que mostra os números negativos de um array.')
print('#' * 120)

n = int(input('Digite a quantidade de elementos que você deseja acrescentar no array (máximo 10).'))
array = []

if n > 10:
    print('Quantidade não permitida')

for i in range(n):
    valor = int(input('Digite os valores desejados positivos e negativos'))
    array.append(valor)

for i in array:
    if i < 0:
        print(i)

print('Fim do programa')